from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Post
from math import ceil

def index(request):

    posts=Post.objects.all()
    # n=len(posts)
    # nslides=n//4 + ceil((n/4)-(n//4))
    count=Post.objects.all().values('category').distinct().count()
    cat=Post.objects.all().values('category').distinct()
    allprod=[]
    for i in range(count):
        prod=Post.objects.filter(category=cat[i]['category']).order_by('-id')
        n=len(posts)
        nslides=n//4 + ceil((n/4)-(n//4))
        allprod.append([prod,range(0,nslides),nslides])
    # if request.user.is_authenticated:
    #     posts=Post.objects.filter(auth=request.user)   
    #     return render(request,'index.html', params )
    # params={'no_of_slides':nslides,'range':range(1,nslides),'posts':posts}
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
    return render(request,'mycart.html');
# def newpage(request):
#     name=request.POST["name"]
#     password=request.POST["password"]
#     if(request.POST["num1"]!='' and request.POST["num2"]!=''):
#         num1=int(request.POST["num1"])
#         num2=int(request.POST["num2"])
#         ans=num1+num2
#     else:
#         ans="Information Invalid"    
#     context={'ans':ans}
#     return render(request,'newpage.html',context)          
