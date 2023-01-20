from django.urls import path
from .views import Registration, UsernameValidation, Login, Logout

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('register/', Registration.as_view(), name="register"),
    path('username_validate/', csrf_exempt(UsernameValidation.as_view()),
         name="username_validate"),
]
