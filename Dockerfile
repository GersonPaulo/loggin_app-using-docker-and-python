# Use an official Python runtime as the base image
# Use the latest stable official Python image (3.12)
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install Python dependencies if any
RUN pip install --no-cache-dir -r requirements.txt || true

# Run the Python script when the container starts
CMD ["python", "__main__.py"]
