#syntax=docker/dockerfile:1
# Use a stable Python version;
FROM python:3.13-alpine

RUN mkdir -p /home/app
# Set the working directory
WORKDIR /home/app

# Copy the current directory contents into the container
COPY . /home/app/
COPY requirements.txt /home/app/requirements.txt

# Recommended (if you have a requirements.txt):
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on (optional but good practice)
#EXPOSE 3000

# Run the application
CMD ["python3", "app.py"]