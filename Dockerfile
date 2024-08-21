# Use the official Ubuntu base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    python3-pip \
    build-essential \
    unixodbc \
    unixodbc-dev \
    msodbcsql18 \
    curl \
    apt-transport-https \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft's APT repository for MSSQL ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean

# Create a directory for the Django app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN python3.11 -m pip install --upgrade pip \
    && python3.11 -m pip install -r requirements.txt

# Copy the Django project files to the working directory
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Set the default command to run Django's development server
CMD ["python3.11", "manage.py", "runserver", "0.0.0.0:8000"]
