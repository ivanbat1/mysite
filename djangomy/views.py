from django.shortcuts import render
from .forms import *
from products.models import *
# Create your views here.

def landing(request):
    name = "CodingMedved"
    current_day = "03.01.2017"
    form = NameForms(request.POST or None)
    if request.POST and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'land/hello.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, 'land/home.html', locals())