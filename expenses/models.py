from django.db import models
from django.contrib.auth.models import User

# Define a Django model for expenses


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=0)
    category = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.category



class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
