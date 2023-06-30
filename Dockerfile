FROM python:3.7.16

RUN mkdir -p /init
RUN mkdir -p /logs
RUN mkdir -p /test

# install the python libraries
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy the source code files to the container
COPY *.py /test
COPY message/*.py /test/message/
COPY exceptions/*.py /test/exceptions/

WORKDIR /test

ENV RABBITMQ_HOST="host.docker.internal"
ENV RABBITMQ_PORT="22222"

CMD [ "python", "-u", "test.py", "${RABBITMQ_HOST}", "${RABBITMQ_PORT}" ]
