from django.shortcuts import render
def index(request):
    return render (request, 'General/index.html')
def shop(request):
    return render (request, 'General/shop.html')