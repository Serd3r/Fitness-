FROM python:3.9-slim

WORKDIR /app

# Install system dependencies if needed (e.g. for building certain python packages)
# RUN apt-get update && apt-get install -y gcc

COPY pyproject.toml .

# Install dependencies
# Using pip to install directly from pyproject.toml if possible, or just manually listing
# For simplicity in this env, manual install of known deps
RUN pip install --no-cache-dir fastapi uvicorn pydantic email-validator

COPY app app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
