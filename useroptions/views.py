from django.shortcuts import render
import os
import json
from django.conf import settings
from .models import UserOptions
from django.contrib import messages


# Create your views here.

def index(request):
    file_path = os.path.join(settings.BASE_DIR, 'currencies.json')

    # getting data from the json file
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    currency_data = [{'name': k, 'value': v} for k, v in data.items()]

    # query for previous preferences or options
    exists = UserOptions.objects.filter(user=request.user).exists()
    user_options = UserOptions.objects.filter(user=request.user).first()

    if request.method == 'GET':
        context = {
            'currencies': currency_data,
            'user_options': user_options,
        }
        return render(request, 'options/index.html', context)

    elif request.method == 'POST':
        currency = request.POST['currency']

        if user_options:
            user_options.currency = currency
            user_options.save()
        else:
            UserOptions.objects.create(user=request.user, currency=currency)

        messages.success(request, 'option saved')

        context = {
            'currencies': currency_data,
            'user_options': user_options,
        }
        return render(request, 'options/index.html', context)

# def index(request):
#     currency_data = []
#     file_path = os.path.join(settings.BASE_DIR, 'currencies.json')
#     # getting data from the json file
#     with open(file_path, 'r') as json_file:
#         data = json.load(json_file)
#         for k, v in data.items():
#             currency_data.append({'name': k, 'value': v})
#     # query for previous prefrences or options
#     exists = UserOptions.objects.filter(user=request.user).exists()
#     user_options = None
#     if exists:
#         user_options = UserOptions.objects.get(user=request.user)
#     if request.method == 'GET':
#         context = {'currencies': currency_data,
#                    'user_options': user_options,
#                    }
#         return render(request, 'options/index.html', context)
#     else:
#         currency = request.POST['currency']
#         if exists:
#             user_options.currency = currency
#             user_options.save()
#         else:
#             UserOptions.objects.create(user=request.user, currency=currency)
#         messages.success(request, 'option saved')
#         context = {'currencies': currency_data,
#                    'user_options': user_options,
#                    }
#         return render(request, 'options/index.html', context)
