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

@siteBluePrint.route('/account')
def account() -> str:
     return render_template('site/account.html')

@siteBluePrint.route('/cart')
def cart() -> str:
     return render_template('site/cart.html')

@siteBluePrint.route('/wishlist')
def wishlist() -> str:
     return render_template('site/wishlist.html')

@siteBluePrint.route('/order')
def order() -> str:
     return render_template('site/order.html')

@siteBluePrint.route('/help')
def help() -> str:
     return render_template('site/help.html')


