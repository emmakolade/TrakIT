paginator = Paginator(expenses, 5)
page_number = request.GET.get('page')
# page_object = paginator.page(page_number)
page_object = Paginator.get_page(paginator, page_number)

# 'page_object': page_object,


# def search_expense(request):
#     if request.method == "POST":
#         search_request = json.loads(request.body).get('searchText')

#         s_expenses = Expense.objects.filter(amount__starts_with=search_request, user=request.user) | Expense.objects.filter(
#             date__starts_with=search_request, user=request.user) | Expense.objects.filter(description__icontains=search_request, user=request.user) | Expense.objects.filter(category__icontians=search_request, user=request.user)

#         data = s_expenses.values()

#         return JsonResponse(list(data), safe=False)


# def search_expense(request):
#     if request.method == "POST":
#         search_request = json.loads(request.body).get('searchText')

#         expenses = Expense.objects.filter(amount__starts_with=search_request, user=request.user) | Expense.objects.filter(
#             date__starts_with=search_request, user=request.user) | Expense.objects.filter(description__icontains=search_request, user=request.user) | Expense.objects.filter(category__icontians=search_request, user=request.user)

#         data = expenses.values()

#         return JsonResponse(list(data), safe=False)


# endpoint visualizing the expense data
# def expense_summary(request):
#     current_date = datetime.date.today()
#     twelvemonth_ago = current_date - datetime.timedelta(days=360)
#      get all expenses for the current user within the past 12 months
#     expenses_date = Expense.objects.filter(user=request.user,
#                                            date__gte=twelvemonth_ago, date__lte=current_date)

#     finalSummary = {}

# # get a list of all unique categories in the expenses
# category_list = list(set(expense.category for expense in expenses_date))

# # iterate through the categories and compute the total amount for each
# for category in category_list:
#     # Filter the expenses by category
#     filtered_category = expenses_date.filter(category=category)
#     # initialize the amount for the category
#     amount = 0
#     # iterate through the expenses and add the amount to the total
#     for item in filtered_category:
#         amount += item.amount
#     # add the total amount for the category to the final summary
#     final_summary[category] = amount

# # Return the final_summary as a JSON response
# return JsonResponse({'expense_category_data': final_summary}, safe=False)

# get all the category in an expense
# def get_category(expense):
#     return expense.category

# category_list = list(set(map(get_category, expenses_date)))

# def get_expense_category_amount(category):
#     amount = 0
#     filtered_category = expenses_date.filter(category=category)
#     for item in filtered_category:
#         amount += item.amount
#     return amount

# for x in expenses_date:
#     for y in category_list:
#         finalSummary[y] = get_expense_category_amount(y)

# return JsonResponse({'expense_category_data': finalSummary}, safe=False)


# def expense_stats(request):
#     current_date = datetime.date.today()
#     twelvemonth_ago = current_date - datetime.timedelta(days=360)
#     # get all expenses for the current user within the past 12 months
#     expenses_date = Expense.objects.filter(user=request.user,
#                                            date__gte=twelvemonth_ago, date__lte=current_date)


#     return render(request, 'expenses/expense_stats.html')
