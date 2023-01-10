from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=0)
    source = models.CharField(max_length=300)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Income'

    def __str__(self):
        return self.source


class Source(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
