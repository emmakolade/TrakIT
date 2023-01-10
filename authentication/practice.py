
from django.contrib.auth.forms import UserCreationForm
from validate_email import validate_email
class EmailValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'invalid email'}, status=400)
        # if usrname exists
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email already exsits.. try another one'}, status=409)

        return JsonResponse({'email_valid': True})


class Registration(View):
    def get(self, request):
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'authentication/register.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

        context = {'form': form}
        return render(request, 'authentication/register.html', context)
