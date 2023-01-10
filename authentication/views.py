from django.views.generic import View
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.validators import validate_email
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str

from .tokens import account_activation_token


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, "thank you for your email confirmation, now you can login into your account")
        return redirect('login')

    messages.error(request, "activation link is invalid")
    return redirect('login')


class Registration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # get user data from the form
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        context = {
            # to pre-populate the form fields with the previous input incase of an error
            'fieldvalues': request.POST
        }

        # check if the username or email already exists in the database.
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 8:
                    messages.error(request, 'password is too short')
                    return render(request, 'authentication/register.html', context)

                # create a new user with the specified username, email, and password.
                user = User.objects.create_user(
                    username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                email_subject = "Activate your account."
                email_message = render_to_string("authentication/email_activation.html", {
                    'user': user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                    'protocol': 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(
                    email_subject,
                    email_message,
                    to=[user.email],
                    
                    
                )
                if email.send():
                    messages.success(
                        request, f'account created sucessfully for {username} please go to your email to confirm and complete the registration')
                else:
                    messages.error(
                        request, f'problem sending activation email to {user.email}')
                return redirect('login')

        return render(request, 'authentication/register.html')


class UsernameValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not username.isalnum():
            return JsonResponse({'username_error': 'username should only contain letters and numbers'}, status=400)
        # if usrname exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exsits.. try another one'}, status=409)


class Login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to authenticate the user with the given credentials
        if username and password:
            user = authenticate(username=username, password=password)

            # If the user is authenticated and active, log them in and redirect them to the home page
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome, ' +
                                 username + ' you are now logged in')
                return redirect('home')

            messages.error(request, 'Invalid credentials, try again')

        # If the user has not provided all the required fields, display an error message
        else:
            messages.error(request, 'Please fill all fields')

        return render(request, 'authentication/login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have been logged out')
        return redirect('base')


# password reset
# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_user = User.objects.filter(Q(email=data))
#             if associated_user.exists():
#                 for user in associated_user:
#                     subject = "password reset requested"
#                     email_template_name = "authentication/password_reset_email.txt"
#                     email_info = {
#                         'email': user.email,
#                         'domain': '127.0.0.1:8000',
#                         'site_name': 'Budg',
#                         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                         'user': user,
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }

#                     email = render_to_string(email_template_name, email_info)
#                     try:
#                         send_mail(subject, email, 'admin@example.com',
#                                   [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     return redirect("/password_reset/done/")

#     password_reset_form = PasswordResetForm()
#     return render(request, 'authentication/password_reset.html')
