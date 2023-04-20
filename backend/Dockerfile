FROM python:3.7.16-bullseye

LABEL maintainer="Claude Manchester"
LABEL version="1.0.0"

# install required packages
COPY sources.list /etc/apt/sources.list
RUN apt update && apt -y upgrade
RUN apt -y install vim openssh-server tree dos2unix
RUN echo "root:123456" | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

WORKDIR /srv/www

# add third-part packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 22/tcp
EXPOSE 2305/tcp

# CMD /etc/init.d/ssh restart
ENTRYPOINT /etc/init.d/ssh restart && bash
