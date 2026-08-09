FROM ubuntu:24.04

RUN apt update && \
    apt install -y openssh-server sudo && \
    mkdir /var/run/sshd

RUN useradd -m devops && \
    echo "devops:devops123" | chpasswd && \
    usermod -aG sudo devops

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]