from flask import Blueprint, render_template, request
from .services import getCategory, getTrendingCategories, getProduct, getTrendingProducts
from models import Product
from sqlalchemy import or_

productBluePrint = Blueprint('product', __name__)




@productBluePrint.route('/')
def index() -> str:
    trendingCategories = []
    trendingCategories = getTrendingCategories()
    trendingProducts = getTrendingProducts()
    return render_template('products/index.html',trendingCategories=trendingCategories,
        products=trendingProducts
    )


@productBluePrint.route('/category/<id>')
def category(id) -> str:
    category = getCategory(id)
    return render_template('products/category.html',category=category)

@productBluePrint.route('/product/<id>')
def product(id) -> str:
    product = getProduct(id)
    return render_template('products/product.html',product=product)

@productBluePrint.route('/search', methods=['POST','GET'])
def search_products():
    search_query = request.form.get('search', '').strip()

    products = []
    if request.method =='POST':
        if search_query:
            products_query = Product.query.filter(Product.ProductName.ilike(f"%{search_query}%"))
            print(products_query)  # Print the query to check if it looks correct
            products = products_query.all()

    print(f"Search Query: {search_query}")  # Check if search term is received
    print(f"Products Found: {products}")  # Check if any products are returned

    return render_template("products/search_results.html", products=products, search_query=search_query)



