from flask import Blueprint, render_template, redirect, url_for, flash
from forms import ContactForm
from models import db, Contact

siteBluePrint = Blueprint('site', __name__)

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
        
        flash('Ditt meddelande har mottagits och sparats!')
        return redirect(url_for('site.contact'))
    return render_template('site/contact.html', form=form)

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')