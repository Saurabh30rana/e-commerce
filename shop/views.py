from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contact
from math import ceil
# Create your views here.
# admin pass Sau@123456
def index(request):
    # product=Product.objects.all()
    # no_of_prod=len(product)
    # nSlides=ceil(no_of_prod/4)
    # print(product)
    # print(no_of_prod)
    # print(nSlides)
    # params={"no_of_slides":nSlides,"range":range(1,nSlides),"product":product}
    # allprod=[[product,range(1,nSlides),nSlides],
    #          [product,range(1,nSlides),nSlides]]

    allprod=[]
    catprods= Product.objects.values('category','id')
    cats={item['category'] for item in catprods}

    for cat in cats:
        prod= Product.objects.filter(category=cat)
        no_of_prod = len(prod)
        nSlides = ceil(no_of_prod / 4)
        allprod.append([prod,range(1,nSlides),nSlides])




    params= {"allprod":allprod}

    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def productView(request,id):
    product= Product.objects.filter(id=id)
    return render(request,'shop/productview.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')
