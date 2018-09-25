# base arch linux image

FROM base/archlinux:2018.09.01

RUN ln -sf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime

RUN pacman -Syy
RUN pacman -S --noconfirm zsh git sudo vim base-devel man

RUN useradd -m -G wheel --create-home docker -s /bin/zsh

COPY sudoers /etc/sudoers
COPY --chown=docker:docker zshrc /home/docker/.zshrc

RUN git config --global user.name "Alec Snyder"
RUN git config --global user.email "linuxbash8@gmail.com"
RUN git config --global alias.co checkout
RUN git config --global alias.br branch
RUN git config --global alias.ci commit
RUN git config --global alias.st status

WORKDIR /home/docker
USER docker
RUN mkdir workspace
WORKDIR /home/docker/workspace