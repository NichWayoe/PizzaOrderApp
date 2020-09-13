from django.db import models

# Create your models here.
class Subs(models.Model):
    sizeOptions = [
        ('S', 'Small'),
        ('L', 'Large')
    ]
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    size = models.CharField(max_length=1, choices=sizeOptions)

    def __str__(self):
        return f"{self.name} - ${self.price}"

class Toppings(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Pasta(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(null=True)
    
    def __str__(self):
        return f"{self.name} - ${self.price}"

class Salads(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField(null=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

class DinnerPlatters(models.Model):
    sizeOptions = [
        ('S', 'Small'),
        ('L', 'Large')
    ]
    name = models.CharField(max_length=20)
    size = models.CharField(choices=sizeOptions, max_length=10)
    price = models.FloatField(null=True)
    def __str__(self):
        return f"{self.name} - ${self.price}"


class RegularPizza(models.Model):
    sizeOptions = [
        ('S', 'Small'),
        ('L', 'Large')
    ]
    toppings = models.ManyToManyField(Toppings)
    size = models.CharField(max_length=10)
    price = models.FloatField(null=True)
    #def price(self):
    #     if (self.size == and self.toppings == 1):
    #         return 13.70
    #     elif (self.toppings == 2):
    #         return 13.70
    #     elif (self.size == and self.toppings == 2):
    #     elif (self.size == and self.toppings == 3):
    #     elif (self.size == and self.toppings == 1):
    #     else:
    #          return 13.70



