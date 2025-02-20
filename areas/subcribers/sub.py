from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_security import current_user, login_required
from forms import ContactForm
from models import db, Contact, NewsletterSubscriber, User
import re

subcribersBluePrint = Blueprint('subcriber', __name__)

# ------------------- NEWSLETTER SIGNUP -------------------
@subcribersBluePrint.route('/newsletter', methods=['POST'])
def newsletter_signup():
    email = request.form.get('email')

    # Regex för validering av e-post
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if email and re.match(email_regex, email):  # Kontrollera att e-posten matchar regex
        # Kolla om mejlen redan finns i databasen
        existing_subscriber = NewsletterSubscriber.query.filter_by(email=email).first()
        if existing_subscriber:
            flash('This email is already subscribed to the newsletter.')
        else:
            # Spara den nya e-postadressen
            new_subscriber = NewsletterSubscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            flash('You have successfully subscribed to the newsletter!')
    else:
        flash('Please provide a valid email address.')

    # Om en användare är inloggad, kontrollera om deras email är prenumererad
    is_subscribed = False
    if current_user.is_authenticated:
        is_subscribed = NewsletterSubscriber.query.filter_by(email=current_user.email).first() is not None

    return render_template('baseTemplate.html', is_subscribed=is_subscribed)
