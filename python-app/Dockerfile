# Use a lightweight official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Expose the application port
EXPOSE 5000

# Specify execution command
CMD ["python", "app.py"]
