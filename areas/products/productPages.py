from flask import Blueprint, render_template, request, url_for, flash, redirect
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts
from models import Category, Product, addCat, addProduct, db
from flask import jsonify


# För att hämta trendiga kategorier


# Definiera Blueprint för produktsidan
productBluePrint = Blueprint('product', __name__)



@productBluePrint.route('/')
def index() -> str:
    # Hämta sorteringsparameter från URL, standardvärde 'latest'
    sort = request.args.get('sort', default='latest')

    # Hämta de heta kategorierna
    trendingCategories = getTrendingCategories()

    # Hämta de heta produkterna baserat på sorteringsparameter
    trendingProducts = getTrendingProducts(sort)

    # Rendera index-sidan och skicka både de heta kategorierna och produkterna
    return render_template('products/index.html', 
                           trendingCategories=trendingCategories, 
                           products=trendingProducts)

    
# Rutt för att visa en kategori med produkter
@productBluePrint.route('/category/<int:id>')
def category(id):
    sort = request.args.get('sort', 'latest')  # Hämta sorteringsparametern från URL
    price_min = request.args.get('price_min', type=float)  # Hämta minsta pris
    price_max = request.args.get('price_max', type=float)  # Hämta högsta pris
    name_filter = request.args.get('name', '')  # Hämta namnfilter

    category, products = getCategory(id, sort, price_min, price_max, name_filter)
    return render_template('products/category.html', category=category, products=products, sort=sort)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    # Hämta produktinformation
    product = getProduct(id)
    
    # Hämta kategori baserat på produktens category_id
    category, _  = getCategory(id)  # Ändra detta till din databasfunktion
    
    print(f"Category: {category}")  # Lägg till en logg för att kontrollera kategoriobjektet
    if category:
        print(f"Category Name: {category.CategoryName}") 

    # Skicka både produkt och kategori till templaten
    return render_template('products/product.html', product=product, category=category)



@productBluePrint.route('/get_sorted_products', methods=['GET'])
def get_sorted_products():
    sort_option = request.args.get('sort', default='latest')
    
    if sort_option == 'price':
        trendingProducts = Product.query.order_by(Product.UnitPrice).limit(8).all()
    elif sort_option == 'name':
        trendingProducts = Product.query.order_by(Product.ProductName).limit(8).all()
    elif sort_option == 'price_desc':
        trendingProducts = Product.query.order_by(Product.UnitPrice.desc()).limit(8).all()
    elif sort_option == 'name_desc':
        trendingProducts = Product.query.order_by(Product.ProductName.desc()).limit(8).all()
    else:
        trendingProducts = Product.query.order_by(Product.ProductID.desc()).limit(8).all()

    # Return the products in JSON format
    products_data = [{'ProductID': product.ProductID, 'ProductName': product.ProductName, 'UnitPrice': product.UnitPrice} for product in trendingProducts]
    return jsonify(products_data)

@productBluePrint.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            # Hämta data från formuläret
            namn = request.form.get('namn')
            supplierid = int(request.form.get('supplierid'))
            categoryid = int(request.form.get('categoryid'))
            quantityperunit = request.form.get('quantityperunit')
            unitprice = float(request.form.get('unitprice'))
            unitsinstock = int(request.form.get('unitsinstock'))
            unitsonorder = int(request.form.get('unitsonorder'))
            reorderlevel = int(request.form.get('reorderlevel'))
            discontinued = int(request.form.get('discontinued'))

            # Anropa funktionen för att lägga till produkten
            addProduct(db, namn, supplierid, categoryid, quantityperunit, unitprice, unitsinstock, unitsonorder, reorderlevel, discontinued)

            flash("Produkten har lagts till!", "success")
            return redirect(url_for('add_product'))  # Omdirigera tillbaka till formuläret

        except Exception as e:
            flash(f"Ett fel uppstod: {str(e)}", "danger")

    return render_template('products/add_product.html')

productBluePrint.route('/add_category', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        try:
            # Hämta data från formuläret
            namn = request.form.get('category_name')
            description = request.form.get('category_description')

            # Anropa funktionen för att lägga till produkten
            addProduct(db, namn, description)

            flash("Category has just been added!", "success")
            return redirect(url_for('products/add_category'))  # Omdirigera tillbaka till formuläret

        except Exception as e:
            flash(f"Ett fel uppstod: {str(e)}", "danger")

    return render_template('products/add_category.html')