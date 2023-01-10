from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from income.models import Income
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse 
import datetime
from django.db.models import Sum, Q

from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie 

# Create your views here.


@login_required(login_url='/authentication/login')
def home(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user=request.user).order_by('-date')

    total_expense = Expense.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']
    total_income = Income.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']

    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    expenses = paginator.get_page(page_number)
    context = {
        'expenses': expenses,
        'total_expense': total_expense,
        'total_income': total_income,
        'categories': categories,
    }
    return render(request, 'expenses/index.html', context)


def base(request):
    return render(request, 'expenses/base.html')


def add_expense(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'expenses/add_expense.html', context)

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
        return redirect('add_expense')

    # Retrieve the date and category from the request data
    date = request.POST.get('date')
    category = request.POST.get('category')

    # Create a new Expense object with the given data
    Expense.objects.create(user=request.user, amount=amount,
                           date=date, category=category, description=description)
    messages.success(request, 'new expense saved succesfully')
    return redirect('home')


def edit_expense(request, id):
    # Get the expense to be edited
    expense = Expense.objects.get(pk=id)

    # Get all available categories
    categories = Category.objects.all()

    if request.method == 'POST':
        # Get the amount, description, and category from the request
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        category = request.POST.get('category')

        # Check if the amount and description are present
        if not amount or not description:
            messages.error(request, 'amount and description are required')
            return redirect('edit_expense')

        # Update the expense with the new values
        expense.user = request.user
        expense.amount = amount
        expense.category = category
        expense.description = description
        expense.save()
        messages.success(request, ' expense upadted succesfully')
        return redirect('home')

    context = {
        'expense': expense,
        'values': expense,
        'categories': categories,
    }

    return render(request, 'expenses/edit_expense.html', context)


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'deleted successfully')
    return redirect('home')


def search_expense(request):
    search_request = request.POST.get('search', '')
    expenses = Expense.objects.filter(
        Q(amount__startswith=search_request) |
        Q(date__startswith=search_request) |
        Q(description__icontains=search_request) |
        Q(category__icontains=search_request),
        user=request.user
    )

    total_expense = Expense.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']
    total_income = Income.objects.filter(
        user=request.user).aggregate(total=Sum('amount'))['total']

    paginator = Paginator(expenses, 15)
    page_number = request.GET.get('page')
    expenses = paginator.get_page(page_number)

    context = {
        'total_expense': total_expense,
        'total_income': total_income,
        'expenses': expenses
    }
    return render(request, 'expenses/search_expense.html', context)


def expense_stats(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses': expenses,
    }
    return render(request, 'expenses/expense_stats.html', context)

# def income_stats(request):
#     income = Income.objects.filter(user=request.user)
#     context={
#         'income': income
#     }
#     return render(request, 'expenses/income_stats.html', context)


@csrf_protect
def link_account(request):
	context = {}
	return render(request, 'myfinance/link-account.html', context)


@ensure_csrf_cookie
def create_link_token(request):
	user = request.user

	if user.is_authenticated:
		data = {
			'user': {
				'client_user_id': str(user.id)
			},
			'products': ["transactions"],
			'client_name': "TrakIT",
			'country_codes': ['US'],
			'language': 'en'
		}

		response = {'link_token': client.post('link/token/create', data)}

		link_token = response['link_token']
		return JsonResponse(link_token)
	else:
		return HttpResponseRedirect('/')
