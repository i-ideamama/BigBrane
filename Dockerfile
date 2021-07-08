FROM python:3.9-slim

# Set pip to have cleaner logs and no saved cache
ENV PIP_NO_CACHE_DIR=false \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  POETRY_VIRTUALENVS_CREATE=false

# Install Poetry and add it to the path
RUN pip install --no-warn-script-location --user poetry
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /app

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

# Install dependencies and lockfile, excluding development dependencies,
RUN poetry install --no-dev --no-interaction --no-ansi

COPY ./bot /app/bot

CMD [ "python", "-m", "bot" ]