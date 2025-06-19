# base image
FROM python:3.9

# workdir
WORKDIR /app

# copy
# COPY ./app
# copy all files to /app in container
COPY . .

# run
RUN pip install -r requirements.txt

# port
EXPOSE 5000

# command  
CMD ["python","app.py"]