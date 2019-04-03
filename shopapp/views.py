from django.shortcuts import render
from shopapp.models import Category, Product

# Create your views here.

def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    contex = {
        'categories': categories,
        'products': products
    }
    return render(request, 'base.html', contex)
