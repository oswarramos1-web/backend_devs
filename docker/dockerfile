# imagen base
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# dependencias del SO necesarias para mysqlclient
RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev gcc libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

# Exponer puerto
EXPOSE 8000

# Entrypoint por defecto (se puede sobreescribir)
CMD ["gunicorn", "src.eficia_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
