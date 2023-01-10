
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('income', views.home, name="income"),
    path('add_income/', views.add_income, name="add_income"),
    path('edit_income/<int:id>', views.edit_income, name="edit_income"),
    path('delete_income/<int:id>', views.delete_income, name="delete_income"),
    path('income_stats/', views.income_stats, name="income_stats"),


    # path('search_income/<int:id>', csrf_exempt(views.search_income), name="search_income"),
]
