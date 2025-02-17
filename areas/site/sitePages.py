from flask import Blueprint, render_template, redirect, url_for, flash
from forms import ContactForm
from models import db, Contact
from flask_security import Security, SQLAlchemyUserDatastore, roles_accepted, auth_required, logout_user, login_user, login_required
from flask_mail import Mail, Message
from flask import current_app

siteBluePrint = Blueprint('site', __name__)
mail = Mail()

#Funktion för formulär i "kontakta oss" sidan
@siteBluePrint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Skapa ny kontaktpost
        new_contact = Contact(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        
        # Lägg till och committa till databasen
        db.session.add(new_contact)
        db.session.commit()
        
        # Skicka bekräftelsemail till användarens ifyllda mejl adress
        msg = Message(
            subject="Tack för ditt meddelande!",
            sender=current_app.config['MAIL_DEFAULT_SENDER'],
            recipients=[form.email.data]
        )
        msg.body = f"Hej {form.name.data},\n\nTack för att du kontaktade oss. Vi har mottagit ditt meddelande och kommer att återkomma så snart som möjligt.\n\nMed vänlig hälsning,\nStefans Webshop"
        
        mail.send(msg)
        
        flash('Ditt meddelande har mottagits och sparats! Ett bekräftelsemail har skickats till din e-postadress.')
        return redirect(url_for('site.contact'))
    return render_template('site/contact.html', form=form)

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
@login_required
def about() -> str:
     return render_template('site/about.html')