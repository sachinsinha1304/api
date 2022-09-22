from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=30,null=False)
    description = models.TextField()
    user = models.ForeignKey('userDetails',null=False,on_delete=models.CASCADE)
    initialPrice = models.IntegerField(default=5000)
    closingDate = models.DateField(null=True)
    image = models.ImageField(upload_to='images/',null=True)
    status = models.BooleanField(default=0)

class userDetails(models.Model):
    name = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30,null=False)
    contact = models.IntegerField()
    role = models.BooleanField(default=0)
    email = models.EmailField()
    mode = models.BooleanField(default = 0)

class Biddings(models.Model):
    itemId = models.ForeignKey('item',null=False,on_delete=models.CASCADE)
    custId = models.ForeignKey('userDetails',null=False,on_delete=models.CASCADE)
    bidd = models.IntegerField(null=False)


class SoldItems(models.Model):
    itemId = models.ForeignKey('item',null=False,on_delete=models.CASCADE)
    custId = models.ForeignKey('userDetails',null=False,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)


