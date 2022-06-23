from email.policy import EmailPolicy
from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage


def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            
        
            
            email = EmailMessage('Subject', 'Mensaje desde Django. \n El usuario  --{}-- cuyo correo es {}, escribe lo siguiente: \n\n {}'.format(nombre,email,contenido), to=['pajile7@gmail.com'])
           
                 
        try:
                        
            email.send()
           
            return redirect("/contacto/?valido")
            
        except: 

            return redirect("/contacto/?HuboError")

    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})
