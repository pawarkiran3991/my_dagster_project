FROM python:3.11-slim

# Set environment variables
ENV DAGSTER_HOME=/opt/dagster/dagster_home

# Create directories
RUN mkdir -p $DAGSTER_HOME
WORKDIR /opt/dagster/app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y \
        gcc \
        g++ \
        git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY pyproject.toml setup.py ./

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -e .

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Run dagster
CMD ["dagster", "dev", "--host", "0.0.0.0", "--port", "3000"]