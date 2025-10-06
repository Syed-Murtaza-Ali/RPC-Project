# Use Python image
FROM python:3.10-slim

# Create app folder
WORKDIR /app

# Copy all project files into container
COPY . .

# Install needed libraries
RUN pip install fastapi uvicorn

# Open port 8080 for access
EXPOSE 8080

# Start the FastAPI app
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
