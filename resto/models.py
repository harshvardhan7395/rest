from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rest(models.Model):
    name_text = models.CharField(max_length=200)
    address_text = models.CharField(max_length=400)

    def __str__(self):
        return self.name_text

    def __str__(self):
        return self.address_text
    
    


class Items(models.Model):
    rest = models.ForeignKey(Rest, on_delete=models.CASCADE)
    dish_text = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return self.dish_text

    def __str__(self):
        return self.price

        

class Order(models.Model):
    rest = models.ForeignKey(Rest,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    item = models.ForeignKey(Items,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


    def __str__(self):
        return self.count
    