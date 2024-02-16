from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render( request , "index.html",  context =  {'page' : "Home" }) 


def about(request):
    peoples = [
        {'name' : 'Abhijeet' , 'age' : 28 } , 
        {'name' : 'Rohan' , 'age' : 21 } , 
        {'name' : 'Ramesh' , 'age' : 18 } , 
        {'name' : 'Abhi' , 'age' : 24 } , 
        {'name' : 'Sandeep' , 'age' : 16 } , 

    ]
    return render(request , "about.html" , context = {'peoples' : peoples , 'page' : "About" })

def contact(request):
    return render(request , "contact.html" , context = {'page' : "Contact" } )

def success_page(request):
    return HttpResponse("this is success page ")