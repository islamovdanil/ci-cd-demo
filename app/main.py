from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Загрузка секретов из Vault (пример)
SECRET_KEY = os.getenv('SECRET_KEY', 'default-key')

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to CI/CD Demo Project",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=os.getenv('DEBUG', 'False') == 'True'
    )
