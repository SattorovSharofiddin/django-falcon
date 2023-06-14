from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)


# class User(AbstractUser):
#     class Status(models.TextChoices):
#         ADMIN = 'admin', 'Admin'
#         CLIENT = 'client', 'Client'
#         VIP_CLIENT = 'vip_client', 'Vip client'
#
#     status = models.CharField(max_length=50, choices=Status.choices, default=Status.CLIENT)
#     email = models.EmailField(unique=True)

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey('app.Category', models.CASCADE)
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    is_premium = models.BooleanField(default=False)
    shopping_cost = models.SmallIntegerField(default=0)
    specification = models.JSONField(default=dict, blank=True)

    # author = models.ForeignKey('app.User', models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/images/', null=True, blank=True)
    product = models.ForeignKey('app.Product', models.CASCADE, 'images')
