from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    image = models.BinaryField(blank=True, null=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    image = models.BinaryField(null=True, blank=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    class Meta:
        db_table = 'cart'
