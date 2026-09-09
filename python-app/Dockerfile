# ---------- Stage 1: build ----------
# Use a full (non-slim) image here only if you need build tools (gcc, etc.)
# for packages with C extensions. Otherwise slim is fine for build too.
FROM python:3.12-slim AS builder

WORKDIR /app

# Copy ONLY requirements first -> this layer only rebuilds when deps change,
# not on every code change. This is the single biggest caching win.
COPY requirements.txt .

# Install into a local target dir so we can copy just the installed
# packages into the final stage (keeps build tools out of the final image)
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt



# ---------- Stage 2: runtime ----------
FROM python:3.12-slim

# Create a non-root user to run the app (never run as root in production)
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Copy installed packages from the build stage (not the build tools themselves)
COPY --from=builder /install /usr/local

# Now copy application code (changes most often -> put it last so it doesn't
# invalidate the dependency-install layer above)
COPY . .

# Own the app dir as the non-root user, then switch to it
RUN chown -R appuser:appuser /app
USER appuser

# Document the port the app listens on (doesn't actually publish it -
# that's what -p / ports: does at run time)
EXPOSE 8000

# Environment variables sensible for containerized Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Adjust to your actual entrypoint (gunicorn/uvicorn/flask run/etc.)
CMD ["python", "app.py"]
