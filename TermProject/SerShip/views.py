from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Subcategory, Item
# Create your views here.

def view(request):
    return render(request, 'SerShip/layout.html')

def SerShip(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    items = Item.objects.all()
    return render(request, "SerShip/index.html", {
        "categories": categories,
        "subcategories": subcategories,
        "items": items
    })