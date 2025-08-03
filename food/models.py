from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=[
("Appetizer","Appetizer"),
("Main Course","Main Course"),
("Desserts","Desserts"),
("Beverages","Beverages")
]
class Item(models.Model):
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name=models.CharField(max_length=50,default="Unknown")
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(default='fallback.png',blank=True)


    

    