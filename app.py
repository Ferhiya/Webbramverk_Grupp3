from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate, upgrade
from forms import ContactForm
from models import db, seedData
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from areas.subcribers.sub import subcribersBluePrint
from areas.subcribers.newsletters import newsletter_blueprint
from flask_security import Security, SQLAlchemyUserDatastore, roles_accepted, auth_required, logout_user, login_user, login_required,current_user
from flask import request, redirect, url_for, flash
from models import db, NewsletterSubscriber,user_datastore,User, Role
from flask_mail import Mail, Message
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
mail = Mail(app)   
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

# Flask-Security Setup (User Authentication)
security = Security(app, user_datastore, register_blueprint=False)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)
app.register_blueprint(subcribersBluePrint)
app.register_blueprint(newsletter_blueprint)


@app.before_request
def load_user_subscription_status():
    if current_user.is_authenticated:
        # Check if the user is in the NewsletterSubscriber table
        is_subscribed = NewsletterSubscriber.query.filter_by(email=current_user.email).first() is not None
    else:
        is_subscribed = False

    # Make it available in templates
    setattr(current_user, "is_subscribed", is_subscribed)
 



# Test för att se att mailhog funkar via denna länk: http://127.0.0.1:5000/send_test_email
# URL för Mailhog: http://localhost:8025/
@app.route('/send_test_email')
def send_test_email():
    msg = Message('Hello world', sender='noreply@example.com', recipients=['test@example.com'])
    msg.body = "This is a test email!"
    mail.send(msg)
    return "Test email sent!"

if __name__  == "__main__":
    
    with app.app_context():
        upgrade()
        seedData(app)
        app.run(debug=True)


