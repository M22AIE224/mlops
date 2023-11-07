#FROM ubuntu:23.10
FROM python:3.9.17
#copy the whole code
COPY . /digits/
#RUN apt-get update
#RUN apt-get install -y  python3 python3-pip
RUN pip3 install -r /digits/requirements.txt
# COPY requirements.txt /requirments.txt
# need python
# no need for conda
# requirement insstallation
# copy all files from root 
RUN mkdir /digits/models
WORKDIR /digits
#RUN ["cd","/digits"]
CMD [ "pytest" ]
RUN Export FLASK_APP = api/app.py
CMD ["flask" , "run"]
