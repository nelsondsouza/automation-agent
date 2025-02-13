# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt (optional)
RUN pip install flask uv

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable for Flask app name
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "app.py"]
