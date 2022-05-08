from unicodedata import category
from django.db import models

class Category(models.Model):
    menu = models.ForeignKey('Menu',on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "categories"

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menu"

class Drinks(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()

    class Meta:
        db_table = "drinks"

class Allegy_drink(models.Model):
    allegy = models.ForeignKey('Allegy',on_delete=models.CASCADE)
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)

    class Meta:
        db_table = "allegy_drink"

class Nutritions(models.Model):
    one_serving_kca = models.DecimalField(max_digits=12, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=12, decimal_places=2)
    saturated_fag_g = models.DecimalField(max_digits=12, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=12, decimal_places=2)
    protein_g = models.DecimalField(max_digits=12, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=12, decimal_places=2)
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)
    size = models.ForeignKey('Sizes',on_delete=models.CASCADE)

    class Meta:
        db_table = "nutritions"

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drinks',on_delete=models.CASCADE)

    class Meta:
        db_table = "images"

class Allegy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allegy"

class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = "sizes"




# Create your models here.
