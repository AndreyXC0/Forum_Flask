from flask import Flask
from flask import render_template
import sqlite3


def ain():
    connection = sqlite3.connect('\data\database.db')
    connection.close()

app = Flask(__name__)


@app.route('/')
def index_html():
    return render_template('index.html')


@app.errorhandler(404)
def handle_bad_request(e):
    return render_template('404.html'), 404


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()