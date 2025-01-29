from flask import Blueprint, render_template, redirect, url_for, flash
from forms import ContactForm

siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('site.contact'))  
    return render_template('site/contact.html', form=form)

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')
