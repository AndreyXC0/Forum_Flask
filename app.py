# from sqlalchemy import create_engine
from flask import Flask
from flask import render_template

'''db_uri = "SQLite://C:/Users/andre/форум/db/forum.db"
eng = create_engine(db_uri)
connection = eng.connect()
outs = eng.execute('SELECT * FROM '"user"'')

print(outs)
connection.close()
'''
forum = Flask(__name__)


@forum.route('/')
def index_html():
    return render_template('index.html')


forum.run(debug=True)
