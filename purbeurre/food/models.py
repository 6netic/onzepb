# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

'''
ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]
'''






class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    nutrition_grade = models.CharField(max_length=1, blank=True, null=True)
    barcode = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    url_pic = models.CharField(max_length=255, blank=True, null=True)
    store = models.CharField(max_length=255, blank=True, null=True)
    prd_cat = models.SmallIntegerField()
    fat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    salt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryProduct(models.Model):
    category = models.OneToOneField(Category, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'category_product'
        unique_together = (('category', 'product'),)


class Favourite(models.Model):
    new_prd_barcode = models.CharField(max_length=255)
    category_product_category = models.ForeignKey(CategoryProduct, models.DO_NOTHING)
    category_product_product_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'favourite'


