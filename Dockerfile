#syntax=docker/dockerfile:1
# Use a stable Python version
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements first for better caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port your app runs on
EXPOSE 3000

# Run the application
CMD ["python3", "app.py"]