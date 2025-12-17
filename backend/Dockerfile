FROM python:3.10-slim

# Убираем интерактивные запросы
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости и GDAL
RUN apt-get update
RUN apt-get install -y --no-install-recommends gdal-bin python3-gdal ffmpeg
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только requirements.txt на этом этапе, чтобы использовать Docker-кеш
COPY requirements.txt .

# Создаем venv и устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем остальной код
COPY . .
