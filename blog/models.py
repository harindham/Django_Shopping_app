from django.db import models
from django.conf import settings
from django.utils.timezone import now

User = settings.AUTH_USER_MODEL

Category_CHOICES = (
    ('Electronics','Electronics'),
    ('Shoes', 'Shoes'),
    ('Kids Wear', 'Kids Wear'),
    ("Men's wear", "Men's wear"),
    ("Women Fashion", "Women Fashion")
)

class Post(models.Model):
    auth = models.ForeignKey(User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        )
    title = models.CharField(max_length=100)
    description=models.TextField()
    img = models.ImageField(upload_to='pics')
    Price = models.IntegerField()
    category = models.CharField(max_length=60, choices=Category_CHOICES) 


class Order(models.Model):
    email = models.EmailField(max_length = 254)
    itemdetails = models.TextField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()
    phonenumber = models.IntegerField()
    totalprice = models.IntegerField()
    noofitems = models.IntegerField()
    status = models.CharField(max_length=100)
    timeoforder = models.DateField(auto_now_add=True)

