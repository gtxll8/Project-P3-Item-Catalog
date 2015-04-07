from flask import Flask, render_template, url_for, request, redirect, flash, jsonify

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Users, Base, SaleItem, Category

engine = create_engine('sqlite:///salesite.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
session = DBSession()

# JSON list all items

# JSOn list only one item



@app.route('/')
@app.route('/forsale/<int:user_id>/')
def salePage(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    items = session.query(SaleItem).filter_by(user_id=user.id)
    return render_template('seller_page.html', user=user, items=items)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
