# Use the official Python 3.11 image.
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependencies file to the container
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install --no-cache-dir poetry

# Configure Poetry
# Avoid creating a virtual environment inside the Docker container
RUN poetry config virtualenvs.create false

# Install dependencies using Poetry
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application's code
COPY . /app

# Command to run the application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
