from django.db import models
from colorfield.fields import ColorField
from djmoney.models.fields import MoneyField
from phone_field import PhoneField


# Create your models here.
class Car(models.Model):
    fuelTypeChoices = (("gas", "gas"), ("diesel", "diesel"))
    gearBoxType = (("manual", "manual"), ("automatic", "automatic"))

    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    fuel_type = models.CharField(max_length=50, choices=fuelTypeChoices)
    gear_box = models.CharField(max_length=50, choices=gearBoxType)
    is_used = models.BooleanField(default=False)
    color = ColorField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    image = models.ImageField(blank=True, null=True)
    status = models.BooleanField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.brand}-{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    description = models.TextField()
    color = ColorField()
    size = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    status = models.BooleanField()
    is_guaranteed = models.BooleanField()
    price = MoneyField(max_digits=14, decimal_places=2, default_currency="USD")
    released_date = models.DateField()
    expiry_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Services(models.Model):
    typeChoices = (
        ("a", "a"),
        ("b", "b"),
        ("c", "c"),
        ("d", "d"),
    )

    type = models.CharField(max_length=2, choices=typeChoices)
    phone = PhoneField()
    car_name = models.CharField(max_length=255)
    reserve_for = models.DateTimeField()

    def __str__(self):
        return f"{self.type} / {self.car_name}"
