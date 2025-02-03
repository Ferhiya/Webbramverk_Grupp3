from flask import Flask,render_template
from models import db, seedData
from flask_migrate import Migrate, upgrade
from areas.site.sitePages import siteBluePrint
from areas.products.productPages import productBluePrint
from flask_security import roles_accepted, auth_required, logout_user
from flask import request, redirect, url_for, flash
from models import db, NewsletterSubscriber


app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)
# user_manager.app = app
# user_manager.init_app(app,db,User)

app.register_blueprint(siteBluePrint)
app.register_blueprint(productBluePrint)


@app.route('/newsletter', methods=['POST'])
def newsletter_signup():
    email = request.form.get('email')
    
    # Check if email is provided and validate it
    if email:
        # Check if the email is already in the newsletter list
        existing_subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('This email is already subscribed to the newsletter.')
        else:
            # Add the email to the database
            new_subscriber = NewsletterSubscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('You have successfully subscribed to the newsletter!')
    else:
        flash('Please provide a valid email.')
    return render_template('products/index.html')


if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData(app)
        app.debug = True
        app.run()


