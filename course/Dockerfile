FROM python:3.13

# create working directory
WORKDIR /app

# copy over requirements.txt and install all required dependencies
COPY requirements.txt .
RUN pip install -r course/requirements.txt

ENV FLASK_APP=course

# copy all files in application
COPY . .

# open up port 80
EXPOSE 80

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"] 

# cli command: docker run -p 80:80 classroom-image