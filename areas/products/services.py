from models import Category, Product

def getTrendingCategories():
    return Category.query.order_by(Category.CategoryID.desc()).paginate(page=1, per_page=4, error_out=False).items

# För att hämta en kategori baserat på ID och sortera produkter
def getCategory(id, sort='latest', price_min=None, price_max=None, name_filter=None):
    category = Category.query.filter(Category.CategoryID == int(id)).first()

    products:Product = Product.query.filter(Product.CategoryId == id)

    # Filtrering av produkter baserat på parametrar
    if price_min:
        products = products.filter(Product.UnitPrice >= price_min)
    if price_max:
        products = products.filter(Product.UnitPrice <= price_max)
    if name_filter:
        products = products.filter(Product.ProductName.like(f'%{name_filter}%'))

    # Sortering baserat på användarens val
    if sort == 'price':
        products = products.order_by(Product.UnitPrice.asc())  # Sortera efter pris
    elif sort == 'name':
        products = products.order_by(Product.ProductName)  # Sortera efter namn
    elif sort == 'name_desc':
        products = products.order_by(Product.ProductName.desc())  # Sortera efter namn, fallande
    elif sort == 'latest':
        products = products.order_by(Product.ProductID.desc())  # Sortera efter senaste (högst ID först)
    elif sort == 'price_desc':
        products = products.order_by(Product.UnitPrice.desc())  # Sortera efter pris, fallande

    # Paginerade resultat
    return category, products.paginate(page=1, per_page=8, error_out=False).items

def getProduct(id):
    return Product.query.filter(Product.ProductID ==id).first()

def getTrendingProducts(sort='latest'):
    # Kontrollera vilket sorteringsalternativ som valts
    if sort == 'price':
        # Sortera efter pris, stigande
        return Product.query.order_by(Product.UnitPrice.asc()).paginate(page=1, per_page=8, error_out=False).items
    elif sort == 'name':
        # Sortera efter produktens namn, alfabetiskt
        return Product.query.order_by(Product.ProductName.asc()).paginate(page=1, per_page=8, error_out=False).items
    elif sort == 'price_desc':
        # Sortera efter pris, fallande
        return Product.query.order_by(Product.UnitPrice.desc()).paginate(page=1, per_page=8, error_out=False).items
    elif sort == 'name_desc':
        # Sortera efter produktens namn, alfabetiskt fallande
        return Product.query.order_by(Product.ProductName.desc()).paginate(page=1, per_page=8, error_out=False).items
    else:
        # Standard: sortera efter senaste produkter (högst ID först)
        return Product.query.order_by(Product.ProductID.desc()).paginate(page=1, per_page=8, error_out=False).items
