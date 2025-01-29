from flask import Blueprint, render_template, redirect, url_for, flash
from forms import ContactForm

siteBluePrint = Blueprint('site', __name__)

#Funktion för formulär i "kontakta oss" sidan
@siteBluePrint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Ditt meddelande har mottagits!')
        return redirect(url_for('site.contact'))  
    return render_template('site/contact.html', form=form)

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')
