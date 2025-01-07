from django.shortcuts import render
from  django.http import JsonResponse
from .models import *
# Create your views here.
def index(request):
    category=foods.objects.all()
    items=foodcategory_items.objects.all()
    chefs1=chefs.objects.all()
    dailyoffer=Dailyoffer.objects.last()
    weeklyoffer=Weeklyoffer.objects.last()
    data={
        'items':items,
        'category':category,
        'chefs':chefs1,
        'weeklyoffer':weeklyoffer,
        'dailyoffer':dailyoffer
    }
    return render(request,'index.html',data)
def menu(request):
    return render(request,'menu.html')
def getdata(request):
    id=request.POST.get('itemid')
    print("hello",id)
    data=foodcategory_items.objects.get(id=id)
    content={
        'name':data.foodcategory_name,
        'price':data.foodcategory_price,
        'description':data.foodcategory_description,
        'image':data.foodcategory_image.url
    }    
    return JsonResponse(content)
def about(requests):

    return render(requests, 'about.html')

def blog(requests):

    return render(requests, 'blog_details.html')

def cart(requests):

    return render(requests, 'cart_view.html')

def checkout(requests):

    return render(requests, 'check_out.html')

def contact(requests):

    return render(requests, 'contact.html')

def dashboard(requests):

    return render(requests, 'dashboard.html')

def footer(requests):

    return render(requests, 'footer.html')

def header(requests):

    return render(requests, 'header.html')

def menu(requests):

    return render(requests, 'menu.html')

def payment(requests):

    return render(requests, 'payment.html')

def signin(requests):

    return render(requests, 'sign_in.html')

def signup(requests):

    return render(requests, 'sign_up.html')

def demo(requests):

    return render(requests, 'demo.html')