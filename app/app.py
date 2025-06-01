from flask import Flask, render_template
import requests

TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'
API_KEY = 'xWrGmmtrRV4sap5jrSTe+Q==rcF97YWAL43iVxnN'

app = Flask(__name__)

# Определяем маршрутизацию.
@app.route('/')
def index():
     # Делаем вызов API — убедитесь, что используете действительный ключ API.
     resp = requests.get(TRIVIA_URL, headers={'X-Api-Key': API_KEY}).json()
     # Получить первый результат викторины, так как API возвращает список результатов.
     trivia = resp[0]
     # Создать HTML-страницу с вопросом и ответом.
     return render_template ('index.html', question=trivia['question'], answer=trivia['answer'])

if __name__ == '__main__':
    # Запустите веб-сервер.
    app.debug = True
    app.run()

