class Cart:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']={}
        self.cart=cart




    def add (self, product):
        if(str(product.id)not in self.cart.keys()):
            self.cart[product.id]={
                'product_id':product.id,
                'model':product.model,
                'price':str(product.price),
                'cant':1,
                'coulor':product.coulor,
                'stock':product.stock,
                'img':product.img.url,
            }
        else:
            for key, value in self.cart.items():
                if key==str(product.id):
                    if value['stock'] <= value['cant']:
                        break
                    else:
                        value['cant']=value['cant']+1
                        value['price']=float(value['price'])+product.price
                        break
                    
        self.save_cart()



    def save_cart(self):
        self.session['cart']=self.cart
        self.session.modified=True



    def delete(self,product):
        product.id=str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()



    def subtract(self, product):
        for key, value in self.cart.items():
            if key==str(product.id):
                value['cant']=value['cant']-1
                value['price']=float(value['price'])-product.price
                if value['cant']<1:
                    self.delete(product)
                break
        self.save_cart()



    def clean_cart(self):
        cart=self.session['cart']={}
        self.session.modified=True


            
   