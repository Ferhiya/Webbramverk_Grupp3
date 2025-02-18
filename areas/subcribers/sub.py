from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_security import login_required
from forms import ContactForm
from models import db, Contact, NewsletterSubscriber, User
import re

subcribersBluePrint = Blueprint('subcriber', __name__)

# ------------------- NEWSLETTER SIGNUP -------------------
@subcribersBluePrint.route('/newsletter/signup', methods=['POST'])
def newsletter_signup():
    print("Newsletter signup route reached!")  # Debugging
    email = request.form.get('email')

    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if email and re.match(email_regex, email):
        existing_subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('This email is already subscribed to the newsletter.')
        else:
            new_subscriber = NewsletterSubscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('You have successfully subscribed to the newsletter!')
    else:
        flash('Please provide a valid email address.')

    return render_template('baseTemplate.html')
