from django.shortcuts import render


# Create your views here.
def homepageview(request):
    return render(request, 'home.html')

def aboutuspage(request):
    return render(request, 'about.html')

def servicepage(request):
    return render(request, 'services.html')