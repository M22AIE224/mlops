# This docker file is to run the pytest 
#FROM ubuntu:23.10
FROM python:3.9.17
#copy the whole code

COPY . /digits/
WORKDIR /digits
#RUN apt-get update
#RUN apt-get install -y  python3 python3-pip
RUN pip3 install -r /digits/requirements.txt
# COPY requirements.txt /requirments.txt
# need python
# no need for conda
# requirement insstallation
# copy all files from root 

#RUN mkdir /digits/models
#WORKDIR /digits
#RUN ["cd","/digits"]
#CMD [ "pytest" ]
#ENTRYPOINT [ "python3" ] 

#EXPOSE 8000
#CMD ["sh","./entrypoint.sh"]
ENV FLASK_APP=api/app
#ENTRYPOINT [ "./api/app" ] 
CMD ["flask" , "run", "--host=0.0.0.0"]
#CMD [ "python" , "m" , "flask" ,"run", "--host=0.0.0.0"]
