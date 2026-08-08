from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Создание метрик
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUESTS = Counter('http_requests_total', 'Total HTTP Requests')

# Декоратор для отслеживания времени выполнения
@REQUEST_TIME.time()
def process_request(t):
    REQUESTS.inc()  # Увеличение счетчика запросов
    time.sleep(t)
    return f"Processed request in {t} seconds"

if __name__ == '__main__':
    # Запуск сервера метрик на порту 8000
    start_http_server(8000)
    while True:
        process_request(random.random())
