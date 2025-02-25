# FastAPI MongoDB Backend

This repository contains a FastAPI application connected to a MongoDB database, configured for local development using Docker.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/) (included with Docker Desktop on Windows and Mac)
- Git (to clone the repository)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/killer-pro/projet_devops
cd projet_devops
```

### 2. Environment Configuration

Create a `.env` file in the root directory with the following variables:

```
# MongoDB Configuration
DATABASE_USER=your_username
DATABASE_HOST=your_db
DATABASE_PASSWORD=your_password
DATABASE_LOCAL_PORT=27017
DATABASE_DOCKER_PORT=27017
MONGO_CONTAINER_URI=mongodb://${DATABASE_USER}:${DATABASE_PASSWORD}@mongodb:27017/
MONGO_URI=127.0.0.1://${DATABASE_USER}:${DATABASE_PASSWORD}@mongodb:27017/
# FastAPI Configuration
APP_LOCAL_PORT=8000
APP_DOCKER_PORT=8000
```

Adjust the values according to your preferences. These environment variables will be used by the Docker Compose configuration.

### 3. Building and Running the Containers

To start both the FastAPI application and MongoDB database:

```bash
docker-compose up -d
```

This command:
- Builds the FastAPI application image using the Dockerfile
- Starts the MongoDB container with the configured credentials
- Creates a Docker network for communication between containers
- Sets up persistent volume for MongoDB data

### 4. Accessing the Application

- The FastAPI application is accessible at: `http://localhost:8000`
- API documentation is available at: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

### 5. Stopping the Containers

To stop the services while preserving data:

```bash
docker-compose down
```

To stop the services and remove volumes (this will delete all database data):

```bash
docker-compose down -v
```

## Development

### Local Development Without Docker

If you prefer to run the FastAPI application locally for development:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application using the provided script:
   ```bash
   python main.py
   ```

This will start the application on `http://127.0.0.1:8000` with hot-reload enabled for development.

## Project Structure

```
fastApiProject/
├── .env                     # Environment variables
├── .dockerignore            # Files to ignore in Docker build
├── app/                     # FastAPI application code
│   ├── routes/              # API route definitions
│   │   └── products.py      # Products endpoints
│   ├── app.py               # Main application entry point
│   ├── database.py          # MongoDB connection and config
│   ├── models.py            # Pydantic models/schemas
│   ├── services.py          # Business logic services
│   └── schemas.py           # Data validation schemas
├── .venv/                   # Virtual environment (not committed)
├── Dockerfile               # Docker configuration for FastAPI
├── docker-compose.yaml      # Docker Compose configuration
├── main.py                  # Local development entry point
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Troubleshooting

### MongoDB Connection Issues

If the FastAPI application cannot connect to MongoDB:

1. Check that both containers are running:
   ```bash
   docker-compose ps
   ```

2. Verify MongoDB logs:
   ```bash
   docker logs mongodb
   ```

3. Ensure the `MONGO_CONTAINER_URI` in the `.env` file matches your MongoDB configuration.

### Port Conflicts

If you encounter port conflicts (ports already in use), modify the local port mappings in your `.env` file.