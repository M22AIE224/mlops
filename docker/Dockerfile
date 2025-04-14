# This docker file is to run the pytest 

# Use a Python base image
FROM python:3.9.17

# Copy all project files into /digits
COPY . /digits/

# Install Python dependencies
RUN pip3 install -r /digits/requirements.txt

# Set working directory
WORKDIR /digits

# Set Flask environment variable
ENV FLASK_APP=api/app

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

#RUN apt-get update
#RUN apt-get install -y  python3 python3-pip
RUN pip3 install -r /digits/requirements.txt
# COPY requirements.txt /requirments.txt
# need python
# no need for conda
# requirement insstallation
# copy all files from root 

#RUN mkdir /digits/models
#RUN ["cd","/digits"]
#CMD [ "pytest" ]
#ENTRYPOINT [ "python3" ] 
#ENTRYPOINT [ "./api/app" ] 
#CMD [ "python" , "m" , "flask" ,"run", "--host=0.0.0.0"]
