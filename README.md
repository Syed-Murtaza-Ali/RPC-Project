# RPC Project

This project demonstrates the implementation of a Remote Procedure Call (RPC) system using FastAPI and Docker. It includes both server and client components, with deployment instructions for Railway.

## Overview

This project implements a simple RPC system with the following features:

- **Server**: Exposes two endpoints:
  - `POST /add`: Adds two numbers.
  - `POST /multiply`: Multiplies two numbers.
- **Client**: Sends requests to the server and displays the results.
- **Dockerized**: The server is containerized using Docker for easy deployment.
- **Timeout Handling**: The client includes a 2-second timeout for requests.

## Project Structure

RPC-Project/
├── server.py # FastAPI server implementation
├── client.py # Python client to interact with the server
├── Dockerfile # Docker configuration for the server
├── requirements.txt # Python dependencies
└── .dockerignore # Files to exclude from the Docker image

## Setup Instructions

### Server Setup

1. Clone the repository:
git clone https://github.com/Syed-Murtaza-Ali/RPC-Project.git
cd RPC-Project

2. Install dependencies:
pip install -r requirements.txt

3. Run the server locally:
uvicorn server:app --host 0.0.0.0 --port 8080
The server will be accessible at http://127.0.0.1:8080.

Client Setup
1. Install the requests library:
pip install requests

2. Run the client:
python client.py

The client will send requests to the server and display the results.

Dockerization

1. Build the Docker image:
docker build -t rpc-server .

2. Run the Docker container:
docker run -p 8080:8080 rpc-server

The server will be accessible at http://localhost:8080.

Deployment on Railway
1. Create a new project on Railway and deploy from GitHub.
2. Set the PORT environment variable to 8080.
3. Railway will automatically build and deploy the project, giving you a public URL for your server.

Usage
Server Endpoints

POST /add: Adds two numbers.

Request:

{
  "x": 2,
  "y": 3
}

Response:

{
  "result": 5
}

POST /multiply: Multiplies two numbers.

Request:

{
  "x": 2,
  "y": 3
}

Response:

{
  "result": 6
}

Client Output
add(2,3) = 5
multiply(4,5) = 20

Timeout Handling
The client includes a 2-second timeout for requests. If the server doesn't respond within this time frame, the client will print:

Request timed out
