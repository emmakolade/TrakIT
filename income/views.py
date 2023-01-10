from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Source, Income
from expenses.models import Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.db.models import Sum
import datetime

# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    sources = Source.objects.all()
    income = Income.objects.filter(user=request.user).order_by('-date')
    total_expense = Expense.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']
    total_income = Income.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']
    
    paginator = Paginator(income, 5)
    page_number = request.GET.get('page')
    income = paginator.get_page(page_number)
    context = {
        'income': income,
        'total_income': total_income,
        'total_expense': total_expense,
    }
    return render(request, 'income/index.html', context)


def add_income(request):
    if request.method == 'GET':
        sources = Source.objects.all()
        context = {'sources': sources}
        return render(request, 'income/add_income.html', context)

    # If the request method is not GET, it must be POST
    # Retrieve the amount from the request data
    amount = request.POST.get('amount')
    # If no amount was provided, add an error message and redirect
    if not amount:
        messages.error(request, 'amount is required')
        return redirect('add_expense')

    # Retrieve the description from the request data
    description = request.POST.get('description')
    # If no description was provided, add an error message and redirect
    if not description:
        messages.error(request, 'description is required')
        return redirect('add_income')

    # Retrieve the date and source from the request data
    date = request.POST.get('date')
    source = request.POST.get('source')

    # Create a new Expense object with the given data
    Income.objects.create(user=request.user, amount=amount,
                          date=date, source=source, description=description)
    messages.success(request, 'income source saved succesfully')
    return redirect('income')


def edit_income(request, id):
    # Get the expense to be edited
    income = Income.objects.get(pk=id)

    # Get all available sources
    sources = Source.objects.all()

    if request.method == 'POST':
        # Get the amount, description, and source from the request
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        source = request.POST.get('source')

        # Check if the amount and description are present
        if not amount or not description:
            messages.error(request, 'amount and description are required')
            return redirect('edit_income')

        # Update the expense with the new values
        income.amount = amount
        income.source = source
        income.description = description
        income.save()
        messages.success(request, ' income upadted succesfully')
        return redirect('income')

    context = {
        'income': income,
        'values': income,
        'source': sources,
    }

    return render(request, 'income/edit_income.html', context)


def delete_income(request, id):
    income = Income.objects.get(pk=id)
    income.delete()
    messages.success(request, 'Income record deleted successfully')
    return redirect('home')


def income_stats(request):
    income = Income.objects.filter(user=request.user)
    context = {
        'income': income
    }
    return render(request, 'income/income_stats.html', context)
