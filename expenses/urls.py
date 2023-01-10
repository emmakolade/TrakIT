
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.base, name="base"),
    path('add_expense/', views.add_expense, name="add_expense"),
    path('edit_expense/<int:id>', views.edit_expense, name="edit_expense"),
    path('delete_expense/<int:id>', views.delete_expense, name="delete_expense"),
    path('search_expense/', (views.search_expense), name="search_expense"),
    # path('search_expense/<int:id>',csrf_exempt(views.search_expense), name="search_expense"),
    path('expense_stats/', views.expense_stats, name="expense_stats"),
    # path('income_stats/', views.income_stats, name="income_stats"),
    # path('expense_summary/', views.expense_summary, name="expense_summary"),
]
