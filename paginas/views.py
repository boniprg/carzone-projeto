from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'paginas/home.html')

def about(request):
    return render(request,'paginas/about.html')

def services(request):
    return render(request,'paginas/services.html')

def contact(request):
    return render(request,'paginas/contact.html')
