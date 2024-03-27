from django.shortcuts import render


# Create your views here.


def shop(request):    
    return render(request, 'shop.html')
def find(request):
    return render(request, 'find.html')

    """ A view to return the index page """
 
def index(request):   
    return render(request, 'home/index.html')