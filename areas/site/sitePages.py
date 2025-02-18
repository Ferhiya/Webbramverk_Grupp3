from flask import Blueprint, render_template

siteBluePrint = Blueprint('site', __name__)

@siteBluePrint.route('/contact')
def contact() -> str:
     return render_template('site/contact.html')

@siteBluePrint.route('/terms')
def terms() -> str:
     return render_template('site/terms.html')

@siteBluePrint.route('/about')
def about() -> str:
     return render_template('site/about.html')

@siteBluePrint.route('/privacy')
def privacy() -> str:
     return render_template('site/privacy.html')

@siteBluePrint.route('/orders')
def orders() -> str:
     return render_template('site/orders.html')

