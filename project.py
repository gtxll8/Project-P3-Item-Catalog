from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
session = DBSession()

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
