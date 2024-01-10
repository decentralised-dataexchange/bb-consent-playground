FROM python:3.10.6-slim-buster

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Update and install dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add poetry package manager
RUN pip install --no-cache-dir poetry

# Copy only requirements to cache them in docker layer
WORKDIR /tests
COPY pyproject.toml .
COPY poetry.lock .

# Project initialization
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy all project
COPY behave.ini .
COPY assets/ assets/
COPY features/ features/
COPY steps/ steps/

CMD ["behave"]