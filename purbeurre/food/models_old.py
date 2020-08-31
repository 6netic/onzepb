# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'category'


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    nutrition_grade = models.CharField(max_length=1, blank=True, null=True)
    barcode = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True, null=True)
    url_pic = models.CharField(max_length=255, blank=True, null=True)
    store = models.CharField(max_length=255, blank=True, null=True)
    prd_cat = models.ForeignKey(Category, models.DO_NOTHING, db_column='prd_cat')
    fat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    saturated_fat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sugar = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    salt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
