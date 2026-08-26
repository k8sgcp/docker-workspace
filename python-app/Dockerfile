
# Use lightweight python base image

FROM python:3.11-slim


# Working directory for the container

WORKDIR /app

# Prevent Python from writing .pyc files & enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1


# Copy requirements first to leverage docker layer caching

COPY requirements.txt .


# Install dependencies without cache to keep image size small

RUN pip install --no-cache-dir -r requirements.txt


# Copy application source code

COPY app.py .


# Create non-root user for security best practices
	

RUN useradd -u 8888 appuser && chown -R appuser:appuser /app
USER appuser


# Expose Flask port

EXPOSE 5000


# Run Flask app
CMD ["python", "app.py"]
