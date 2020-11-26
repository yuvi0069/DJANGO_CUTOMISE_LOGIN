from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateField(auto_now_add=True , null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),('Out door','Out door'))
    name=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    descripition=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    date_created=models.DateField(auto_now_add=True , null=True)
class Order(models.Model):
    STATUS=(('pending','pending'),
            ('out for delievery','out for delievery'),
            ('delivered','delivered'))
    #customer=models.CharField(max_length=200,null=True)
    #product=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    date_created=models.DateField(auto_now_add=True , null=True)
class Video(models.Model):
    video=models.FileField(upload_to='accounts/static/%y')


