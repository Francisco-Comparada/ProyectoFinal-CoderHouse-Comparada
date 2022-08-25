from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Order, Order_line
from Cart.cart import Cart
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

@login_required(login_url='/User/login')
def process_order(request):
    order=Order.objects.create(user=request.user)
    cart=Cart(request)
    order_line=list()
    for key,value in cart.cart.items():
        order_line.append(Order_line(
            product_id=key,
            cant=value['cant'],
            user=request.user,
            order=order,
        ))

    Order_line.objects.bulk_create(order_line)

    send_mail_(
        order=order,
        order_line=order_line,
        name_user=request.user.username,
        email_user=request.user.email,
        )

    messages.success(request,'Pedido realizado con exito')

    return redirect('/Cart/cart/')

def send_mail_(**kwargs):
    subject='Gracias por el pedido Urbans Sneakers'
    
    message=render_to_string('mail/orders.html',{
        'order':kwargs.get('order'),
        'order_line':kwargs.get('order_line'),
        'name_user':kwargs.get('name_user'),
        'email_user':kwargs.get('email_user')
    })

    message_text=strip_tags(message)
    from_mail='francisco.comparada@gmail.com'
    to=kwargs.get('email_user')

    send_mail(subject,message_text,from_mail,[to],html_message=message)