FROM ubuntu:18.04

RUN apt-get update && apt-get install build-essential -y

# set the working directory in the container
WORKDIR /usr/app

# copy the content of the local src directory to the working directory
COPY . .

RUN gcc server.c -o srvr

# command to run on container start
CMD [ "./srvr" ]
