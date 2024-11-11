# Use a Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (if you have one) and install dependencies
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . /app

# Expose the port that Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "application.py"]
