from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='blog-index'),
    path('create-post',views.crtpost,name='blog-create-post'),
    path('mycart',views.mycart,name='blog-mycart')
]
