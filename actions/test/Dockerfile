FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev xz-utils libxext-dev libssl-dev libxrender1 zip unzip xvfb wget libfontconfig1

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
