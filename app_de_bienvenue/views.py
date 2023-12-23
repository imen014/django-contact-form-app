from django.shortcuts import render
from django.http import HttpResponse
from app_de_bienvenue.forms import FormContact

def welcome1(request):
    return render(request,
                  'app_de_bienvenue/page_de_bienvenue.html')

def FormContact1(request):
    form = FormContact()
    if request.method == "POST":
        form = FormContact(request.POST)
        if form.is_valid():
            
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return render(request, 'app_de_bienvenue/confirmation.html', {'nom':nom, 'email':email,'message':message})
        
    else:
        contenu = "verifier les données"
        return HttpResponse(contenu)
        #form = FormContact()
    
    return render(request,
                  'app_de_bienvenue/myform.html',
                  {'form':form})