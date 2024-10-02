# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app


# Copy only the requirements file initially to leverage Docker cache
COPY requirements.txt requirements.txt
COPY entrypoint.sh .

# ENV PIP_CONSTRAINT=constraints.txt

RUN apt-get update && apt-get install -y gdal-bin libgdal-dev


# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install psycopg2  

# Copy the rest of the application code
COPY /online_library_system .

# Create a logs directory and grant permissions
RUN mkdir logs && chmod 777 logs

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Modify your entrypoint.sh or create a new script to run Celery workers / beat alongside your application
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Define the default command to run when the container starts.
# You might want to modify this to start both your Django app and Celery workers
CMD ["/entrypoint.sh"]

