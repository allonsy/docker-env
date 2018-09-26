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
        "-it", 
        "--mount",
        f"type=bind,source={cwd},target=/home/docker/workspace",
        container,
        "zsh"    
    ])

def build_container(container, *tags):
    print("building container: " + container + " with tags: " + str(tags))
    os.chdir(os.path.join(file_dir, container))
    cmd = ["docker", "build", "-t", container]
    for tag in tags:
        cmd.append("-t")
        cmd.append(tag)
    cmd.append(".")
    run(cmd)

if ARGS[1] == "build":
    build_container(ARGS[2], *ARGS[3:])
else:
    run_container_interactive_mount(ARGS[1])
