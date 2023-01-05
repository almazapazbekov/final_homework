from django.db import models
from account.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'category: {self.name}'


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'name: {self.name},price: {self.price}, profile: {self.profile}'


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'item: {self.item}, quantity: {self.quantity}, profile: {self.profile}'
