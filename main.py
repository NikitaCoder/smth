from flask import Flask
import random

app = Flask(__name__)

facts_list = 'Самая крупная жемчужина в мире достигает 6 килограммов в весе.', 'Среднее облако весит порядка 500 тонн, столько же весят 80 слонов.', 'В Саудовской Аравии нет рек', 'Лимон содержит больше сахара, чем клубника.'

@app.route("/")
def hello_world():
    return f'<h1>Привет!Если хочешь увидеть интересные факты нажми на кнопку ниже</h1> <a href="/end">Посмотреть случайный факт!</a>'


@app.route("/end")
def end():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)