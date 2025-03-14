# Use the official Python image from the Docker Hub
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80 514

# Define environment variable
ENV WEBHOOK_PORT 80
ENV SYSLOG_PORT 514

# Run app.py when the container launches
CMD ["python", "main.py"]