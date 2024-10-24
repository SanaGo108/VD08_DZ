from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        quote_data = response.json()
        return quote_data['content'], quote_data['author']
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при запросе цитаты: {e}")
        return "Не удалось получить цитату", "Неизвестный автор"

@app.route('/')
def index():
    quote, author = get_random_quote()
    return render_template("index.html", quote=quote, author=author)

if __name__ == '__main__':
    app.run(debug=True)
