# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install Flask

# Expose port 5000 for Flask
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]

# Build the Docker image
docker build -t flask-login-app .

# Run the container with a volume mounted to store logs in /var/lib/docker/
docker run -d -p 5000:5000 -v /var/lib/docker:/var/lib/docker flask-login-app
