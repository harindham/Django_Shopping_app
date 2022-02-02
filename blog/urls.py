from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='blog-index'),
    path('create-post',views.crtpost,name='blog-create-post'),
    path('contactus',views.contactus,name='blog-contactus'),
    path('aboutus',views.aboutus,name='blog-aboutus'),
    path('myorders',views.myorders,name='blog-myorders'),
    path('mycart',views.mycart,name='blog-mycart'),
    path('placeorder',views.placeorder,name='blog-placeorder')
]
