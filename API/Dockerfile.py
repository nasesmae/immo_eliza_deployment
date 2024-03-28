# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set the working directory in the container
WORKDIR /api

# Copy the current directory contents into the container at /api
COPY . /api

# Copy requirements.txt and install the Python dependencies
COPY requirements.txt /api
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable to hold the command to run Uvicorn
ENV UVICORN_CMD="uvicorn --host 0.0.0.0 --port 8000 api.app:app"

# Run Uvicorn when the container launches
ENTRYPOINT ["sh", "-c", "$UVICORN_CMD"]


