import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, request, redirect, url_for, \
    send_from_directory

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

# testing start
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            editedItem = session.query(SaleItem).filter_by(id=2).one()
            editedItem.image_name = file.filename
            session.add(editedItem)
            session.commit()
            flash("New image added !")
            return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/show/<filename>')
def uploaded_file(filename):
    filename = url_for('static', filename=filename)
    items = session.query(SaleItem).filter_by(user_id=1)
    return render_template('template.html', filename=filename, items=items)

@app.route('/static/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# testing stop

@app.route('/')
@app.route('/forsale/<int:user_id>/')
def sellerPage(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    items = session.query(SaleItem).filter_by(user_id=user.id)
    return render_template('seller_page.html', user=user, items=items)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
