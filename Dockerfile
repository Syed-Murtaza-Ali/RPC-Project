# Use Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install fastapi uvicorn

# Expose port 8080
EXPOSE 8080

# Start the server
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]