from Cart.cart import Cart
def total_cart_amount(request):
    total=0
    if request.user.is_authenticated:
        if 'cart' in request.session:
            for key,value in request.session['cart'].items():
                total = total +(float(value['price']))
    return{'total_cart_amount':total}

def total_product(request):
    total=0
    if request.user.is_authenticated:
        if 'cart' in request.session:
            for key,value in request.session['cart'].items():
                total = total +(int(value['cant']))
    return{'total_product':total}