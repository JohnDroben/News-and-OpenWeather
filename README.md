# News-and-OpenWeather
Trivia Challenge - Приложение-викторина
Скриншот приложения

Обзор
Trivia Challenge - веб-приложение, которое показывает случайные вопросы викторины, используя API-Ninjas Trivia API. Приложение построено на Flask и Bootstrap 5 с современным пользовательским интерфейсом, плавными анимациями и адаптивным дизайном.

Основные возможности
🎯 Динамическая генерация вопросов викторины

💡 Интерактивное открытие ответов с анимацией

🔄 Обновление вопросов в один клик

📱 Полностью адаптивный дизайн

🎨 Современный UI в стиле glass-morphism

⚡ Быстрое и легковесное приложение

Технологический стек
Бэкенд: Python 3, Flask

Фронтенд: HTML5, CSS3, Bootstrap 5

API: API-Ninjas Trivia API

Зависимости: requests, Flask, python-dotenv

Начало работы
Предварительные требования
Python 3.8+

Менеджер пакетов Pip

Аккаунт на API-Ninjas (доступен бесплатный тариф)

Установка
Клонируйте репозиторий:

bash
git clone https://github.com/ваш-username/trivia-app.git
cd trivia-app
Создайте и активируйте виртуальное окружение:

bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
Установите зависимости:

bash
pip install -r requirements.txt
Получите API-ключ:

Зарегистрируйтесь на api-ninjas.com

Получите API-ключ в личном кабинете

Создайте файл .env:

env
API_KEY=ваш_api_ключ_здесь
Запуск приложения
bash
python app.py
Откройте в браузере http://localhost:5000 для доступа к приложению.

Структура проекта
trivia-app/
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   
│   └── app.py
├── .env
├── requirements.txt
└── README.md
Настройка
Вы можете настроить приложение, изменив параметры в app.py:

python
# API endpoint
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

# Количество получаемых вопросов (API может возвращать несколько)
QUESTIONS_COUNT = 1

# Таймаут запросов (секунды)
REQUEST_TIMEOUT = 5
Документация API
Приложение использует API-Ninjas Trivia API со следующими параметрами:

category: Общие знания (можно настроить)

limit: 1 вопрос за запрос

difficulty: Случайная сложность

Разработка
Вклады приветствуются! Следуйте этим шагам:

Форкните репозиторий

Создайте ветку для вашей функции (git checkout -b feature/ваша-функция)

Зафиксируйте изменения (git commit -m 'Добавлена новая функция')

Запушьте ветку (git push origin feature/ваша-функция)

Создайте pull request

Лицензия
Этот проект лицензирован по лицензии MIT - подробности в файле LICENSE.

Скриншоты
Вид на ПК	Мобильный вид
ПК	Мобильный
Благодарности
API-Ninjas за API викторины

Bootstrap за CSS-фреймворк

Flask за веб-фреймворк

Наслаждайтесь проверкой своих знаний со случайными вопросами викторины! 🧠✨