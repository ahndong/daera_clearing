# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Argument for backend endpoint
ARG BACKEND_ENDPOINT_ARG

# Environment variable to store the backend endpoint
ENV BACKEND_ENDPOINT=$BACKEND_ENDPOINT_ARG

# Install Poetry
# We're using --no-root to avoid Poetry installing the package itself in editable mode.
# That is, we only want to install dependencies.
RUN pip install --no-cache-dir poetry

# Copy the Python dependencies file to the container
COPY pyproject.toml poetry.lock* /usr/src/app/

# Install the project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application's code
COPY . /usr/src/app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
