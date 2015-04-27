# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the CRUDs are done

import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, request, redirect, url_for, \
    send_from_directory, make_response

from config import CONFIG
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Users, Base, SaleItem, Category
from flask.ext.login import AnonymousUserMixin

# Initialize the Flask application
app = Flask(__name__)

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'development', report_errors=False)

# This is the path to the upload directory
UPLOAD_FOLDER = './static'
# These are the extension that we are accepting to be uploaded
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

engine = create_engine('sqlite:///salesite.db')
# Bind the engine to the metadata of the Base class so that the
# declarative can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
session = DBSession()

# JSON list all items

# JSOn list only one item


# User class
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# Home route
@app.route('/')
def index():
    items = session.query(SaleItem).all()
    return render_template('index.html', items=items)


@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    """
    Login handler, must accept both GET and POST to be able to use OpenID.
    """

    # We need response object for the WerkzeugAdapter.
    response = make_response()

    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), provider_name)

    # If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            print 'user updated'
            # We need to update the user to get more info.
            result.user.update()
            # Check if this user is already in db
            user = session.query(Users).filter_by(social_id=result.user.id).first()
            if user:
                print "already registered"
            else:
                new_user = Users(social_id=result.user.id, name=result.user.name)
                session.add(new_user)
                session.commit()
                flash("New user account added !")

        print result.user.name
        # The rest happens inside the template.
        return render_template('login.html', result=result, email=result.user.email)

    # Don't forget to return the response.
    return response


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basically show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))


# Add new image to product
@app.route('/forsale/<int:user_id>/<int:item_id>/upload/', methods=['GET', 'POST'])
def upload_file(item_id, user_id):
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print item_id
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            editedItem = session.query(SaleItem).filter_by(id=item_id).one()
            editedItem.image_name = file.filename.replace(" ", "_")
            session.add(editedItem)
            session.commit()
            flash("New image added !")
            return redirect(url_for('sellerPage', user_id=user_id))


@app.route('/static/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


# Add new items
@app.route('/')
@app.route('/forsale/<user_id>/new/', methods=['GET', 'POST'])
def newSaleItem(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    if request.method == 'POST':
        newItem = SaleItem(name=request.form['name'], description=request.form['description'],
                           price=request.form['price'], user_id=user_id)
        session.add(newItem)
        session.commit()
        flash("New sale item created !")
        item = session.query(SaleItem).order_by(SaleItem.id.desc()).first()
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            editedItem = session.query(SaleItem).filter_by(id=item.id).one()
            editedItem.image_name = file.filename.replace(" ", "_")
            session.add(editedItem)
            session.commit()
            flash("New image added !")
        return redirect(url_for('sellerPage', user_id=user_id))
    else:
        return render_template('newitem.html', user=user, user_id=user_id)


# Edit items
@app.route('/')
@app.route('/forsale/<int:user_id>/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(user_id, item_id):
    user = session.query(Users).filter_by(id=user_id).first()
    editeditem = session.query(SaleItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editeditem.name = request.form['name']
        if request.form['description']:
            editeditem.description = request.form['description']
        if request.form['price']:
            editeditem.price = request.form['price']
        session.add(editeditem)
        session.commit()
        flash("Change saved !")
        product_file = request.files['file']
        if product_file and allowed_file(product_file.filename):
            # Remove the old file from folder
            if editeditem.image_name and os.path.isfile(
                    os.path.join(app.config['UPLOAD_FOLDER'], editeditem.image_name)):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], editeditem.image_name))
            filename = secure_filename(product_file.filename)
            product_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            editeditem.image_name = product_file.filename.replace(" ", "_")
            session.add(editeditem)
            session.commit()
            flash("New image added !")
        return redirect(url_for('sellerPage', user_id=user_id))
    else:
        return render_template('edititem.html', user=user, user_id=user_id, item=editeditem)


# Delete items
@app.route('/forsale/<user_id>/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(user_id, item_id):
    deletedItem = session.query(SaleItem).filter_by(id=item_id).one()
    item = session.query(SaleItem).filter_by(id=item_id).one()
    print item_id
    if request.method == 'POST':
        # delete the file from the upload folder too
        if item.image_name and os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], item.image_name)):
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], item.image_name))
        session.delete(deletedItem)
        session.commit()
        flash("Item deleted !")
        return redirect(url_for('sellerPage', user_id=user_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('deleteitem.html', user_id=user_id, item_id=item_id, item=deletedItem)


# Main seller's page
@app.route('/')
@app.route('/forsale/<int:user_id>/')
def sellerPage(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    items = session.query(SaleItem).filter_by(user_id=user_id)
    return render_template('seller_page.html', user=user, items=items)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
