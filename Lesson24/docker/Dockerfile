FROM selenium/standalone-chrome
USER root
COPY . /
RUN chmod +x ./entrypoint.sh
RUN apt-get update && apt-get install -y git && sudo apt-get install -y python3-pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
ENTRYPOINT ["/entrypoint.sh"]

