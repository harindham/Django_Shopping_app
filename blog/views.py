from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Post,Order
from math import ceil
import json

def index(request):
    posts=Post.objects.all()
    # n=len(posts)
    # nslides=n//4 + ceil((n/4)-(n//4))
    count=posts.values('category').distinct().count()
    cat=posts.values('category').distinct()
    allprod=[]
    for i in range(count):
        prod=Post.objects.filter(category=cat[i]['category']).order_by('-id')
        n=len(prod)
        nslides=n//4 + ceil((n/4)-(n//4))
        allprod.append([prod,range(0,nslides),nslides])
    # if request.user.is_authenticated:
    #     posts=Post.objects.filter(auth=request.user)   
    #     return render(request,'index.html', params )
    # params={'no_of_slides':nslides,'range':range(1,nslides),'posts':posts}
    params={'allprod':allprod}
    return render(request,'index.html', params)


def searchfunc(item,searchitem):
    searchitem=searchitem.lower()
    if searchitem in item.title.lower() or searchitem in item.category.lower() or searchitem in item.description.lower():
        return True
    else:
        return False


def search(request):
    if request.method == 'POST':
        searchitem=request.POST.get('searchitem')
        print(searchitem)
        posts=Post.objects.all()
        # n=len(posts)
        # nslides=n//4 + ceil((n/4)-(n//4))
        count=posts.values('category').distinct().count()
        cat=posts.values('category').distinct()
        allprod=[]
        for i in range(count):
            prodtemp=Post.objects.filter(category=cat[i]['category']).order_by('-id')
            prod=[item for item in prodtemp if searchfunc(item,searchitem)]
            n=len(prod)
            nslides=n//4 + ceil((n/4)-(n//4))
            if len(prod) != 0:
                allprod.append([prod,range(0,nslides),nslides])
        params={'allprod':allprod}
        return render(request,'index.html', params)        


def crtpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('image') and request.POST.get('category'):
            post=Post()
            post.auth=request.user
            post.title = request.POST.get('title')
            post.description = request.POST.get('description')
            post.img = request.POST.get('image')
            post.Price = request.POST.get('Price')
            post.category = request.POST.get('category')
            post.save()
            return redirect('/')
        else:
            messages.info(request,'Invalid Information')
            return redirect('/create-post')      

    else:
        return render(request,'create-post.html')      



def mycart(request):       
    return render(request,'mycart.html')


def aboutus(request):       
    return render(request,'aboutus.html')

def contactus(request):       
    return render(request,'contactus.html')  

def myorders(request):  
    allorders=Order.objects.filter(email=request.user.email)
    dic={}
    for index in allorders:
        dic[index.id]=json.loads(index.itemdetails)
    print(dic)    
    return render(request,'myorders.html',{'allorders':allorders,'dic':dic})      


def placeorder(request):


    if request.method == 'POST':
        if request.POST.get('address1') and request.POST.get('phonenumber') and request.POST.get('itemdetails') and request.POST.get('firstname'):
            order=Order()
            order.email=request.user.email
            order.itemdetails = request.POST.get('itemdetails') 
            order.firstname = request.POST.get('firstname')
            order.lastname = request.POST.get('lastname')
            order.address = request.POST.get('address1') +' '+ request.POST.get('address2')+' '+request.POST.get('city')+', '+request.POST.get('state')+' '+request.POST.get('zip')
            order.phonenumber = request.POST.get('phonenumber')
            order.totalprice=request.POST.get('totprice')
            order.noofitems=request.POST.get('noofitems')
            order.status='Waiting...'
            order.save()
            thankmessage="Thanks for shopping with us. Your order id is "+str(order.id)
            return render(request,'order-page.html',{'thank':thankmessage})
        else:
            messages.info(request,'Invalid Information')
            return redirect('/placeorder')      

    else:        
        return render(request,'order-page.html');       
