FROM rappdw/docker-java-python:openjdk1.8.0_171-python3.6.6


RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin

RUN gcloud components install pubsub-emulator
RUN gcloud components update
RUN gcloud components install beta


RUN export CLOUDSDK_CORE_DISABLE_PROMPTS=1
RUN gcloud components update 

RUN mkdir /python task
COPY . /python-task

