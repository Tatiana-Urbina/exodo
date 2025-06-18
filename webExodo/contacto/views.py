from django.shortcuts import render, redirect 
from django.core.mail import send_mail 
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactoForm

# Create your views here.
def contacto(request):

    contato_form = ContactoForm()

    if request.method == 'POST':
        contato_form = ContactoForm(data=request.POST)
        if contato_form.is_valid():
            nombre = contato_form.cleaned_data['nombre']
            mail = contato_form.cleaned_data['mail']
            mensaje = contato_form.cleaned_data['mensaje']

            #contenido del correo
            asunto = f'Mensaje de {nombre} desde tu sitio web'
            mensaje_completo = f'Nombre: {nombre}\nEmail: {mail}\nMensaje:\n{mensaje}'
            remitente = mail
            destinatario = ['urbinatatiana077@gmail.com']


            # Enviar el correo
            try:
                send_mail(asunto, mensaje_completo, remitente, destinatario)
                return redirect(reverse('contacto')+"?ok")
            except:
                return redirect(reverse('contacto')+"?fail")

    return render(request, "contacto/contacto.html", {'form': contato_form})