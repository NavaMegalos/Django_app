from django.db import models

class Brand(models.Model):
    name = models.TextField(max_length=150)

class ProductPresentation(models.Model):
    name = models.TextField(max_length=150)
    
class Product(models.Model):
    price = models.FloatField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    product_presentation = models.ForeignKey("ProductPresentation", on_delete=models.CASCADE)
