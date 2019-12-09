from django.db import models

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

        