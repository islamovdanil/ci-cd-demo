# Базовый образ для сборки
FROM alpine:latest

# Установка зависимостей
RUN apk add --no-cache \
    python3 \
    py-pip \
    git

# Установка Helm
RUN pip3 install kubernetes

# Копирование чарта
COPY . /charts/ci-cd-demo

# Установка чарта как зависимости
RUN helm dependency build /charts/ci-cd-demo
