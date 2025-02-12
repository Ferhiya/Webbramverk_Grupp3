from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate, upgrade
from forms import ContactForm
from models import db, seedData
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from areas.subcribers.sub import subcribersBluePrint
from flask_security import Security, SQLAlchemyUserDatastore, roles_accepted, auth_required, logout_user, login_user, login_required
from flask import request, redirect, url_for, flash
from models import db, NewsletterSubscriber,user_datastore,User, Role
import re
import os
from dotenv import  load_dotenv
load_dotenv()


app = Flask(__name__)
app.config.from_object('config.ConfigDebug')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/shop20220128'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SECURITY_PASSWORD_SALT'] = os.getenv("SECURITY_PASSWORD_SALT")


db.app = app
db.init_app(app)
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

# Flask-Security Setup (User Authentication)
security = Security(app, user_datastore, register_blueprint=False)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)
app.register_blueprint(subcribersBluePrint)

@app.route("/")
@login_required
def startpage():
    return render_template("products/index.html")




if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.run(debug=True)


