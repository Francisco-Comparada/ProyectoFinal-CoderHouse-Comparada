from django.shortcuts import render, redirect
from .forms import form_contact
from django.core.mail import EmailMessage

def contact(request):
    form=form_contact()
    if request.method=='POST':
        form=form_contact(data=request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')

            #en la linea ['urbanssneakers22@gmail.com'] debremos de poner el mail que pusimos en el settings
            email=EmailMessage(subject,'El usuario {} mail {} mensaje: \n\n {} '.format(name,email,message),
            email,['urbanssneakers22@gmail.com'],reply_to=[email])
             # descomentar para utilizar funcion de mail 
            """ try:
                email.send()
                return redirect('/Contact/contact/?valido')
            except:
                return redirect('/Contact/contact/?novalido') """

           

    return render (request,'Contact/contact.html',{'form':form})
