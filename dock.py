import sys
import os
from subprocess import run

ARGS = sys.argv

file_dir = os.path.dirname(os.path.realpath(__file__))

def get_cwd():
    return os.getcwd()

def run_container_interactive_mount(container):
    cwd = get_cwd()
    run([
        "docker", 
        "run",
        "--rm",
        "-it", 
        "--mount",
        f"type=bind,source={cwd},target=/home/docker/workspace",
        container,
        "zsh"    
    ])

def build_container(container, *tags, clean=False):
    print("building container: " + container + " with tags: " + str(tags))
    os.chdir(os.path.join(file_dir, container))
    cmd = ["docker", "build", "-t", container]
    if clean:
        cmd.append("--no-cache")
    for tag in tags:
        cmd.append("-t")
        cmd.append(tag)
    cmd.append(".")
    run(cmd)

def run_oneshot(container, *cmds):
    cmd = ["docker", "run", container]
    for c in cmds:
        cmd.append(c)
    run(cmd)

def clean():
    print("Pruning system...")
    cmd_containers = ["docker", "system", "prune", "-f"]
    run(cmd_containers)
    
def edit(container):
    cmd = ["vim", os.path.join(file_dir, container, "Dockerfile")]
    run(cmd)



if ARGS[1] == "build":
    build_container(ARGS[2], *ARGS[3:])
elif ARGS[1] == "clean-build":
    build_container(ARGS[2], *ARGS[3:], clean=True)
elif ARGS[1] == "run":
    run_oneshot(ARGS[2], *ARGS[3:])
elif ARGS[1] == "clean":
    clean()
elif ARGS[1] == "edit":
    edit(ARGS[2])
else:
    run_container_interactive_mount(ARGS[1])
