from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

Category_CHOICES = (
    ('electronics','electronics'),
    ('shoes', 'shoes'),
    ('tshirt','tshirt'),
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


