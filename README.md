# Flask Application with MongoDB

This is a Flask web application that uses MongoDB as its database backend. The application is containerized using Docker and uses Docker networks for communication between services.

## Architecture

The application consists of three main components:
1. Flask web application
2. MongoDB database
3. Mongo Express (web-based MongoDB admin interface)

## Prerequisites

- Docker
- Docker Compose

## Configuration

Before running the application, you need to modify the following parameters in the `docker-compose.yml` file:

1. MongoDB Configuration:
   ```yaml
   environment:
     - MONGO_INITDB_ROOT_USERNAME=admin  # Change this to your desired username
     - MONGO_INITDB_ROOT_PASSWORD=admin  # Change this to your desired password
   ```

2. Mongo Express Configuration:
   ```yaml
   environment:
     - ME_CONFIG_MONGODB_ADMINUSERNAME=admin  # Must match MongoDB username
     - ME_CONFIG_MONGODB_ADMINPASSWORD=admin  # Must match MongoDB password
   ```

3. Flask Application Configuration:
   ```yaml
   environment:
     - MONGODB_URI=mongodb://admin:admin@mongodb:27017/  # Update with your MongoDB credentials
   ```

## Running the Application

1. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

2. Access the services:
   - Flask Application: http://localhost:3000
   - Mongo Express: http://localhost:8081
   - MongoDB: mongodb://localhost:27017

## Stopping the Application

To stop the application:
```bash
docker-compose down
```

## Network Configuration

The application uses a Docker network named `mongo-network` to allow communication between the containers. This network is automatically created when you run `docker-compose up`.

## Security Note

Remember to change the default credentials before deploying to production. The current configuration uses default values for demonstration purposes. 