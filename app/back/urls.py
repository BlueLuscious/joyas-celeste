from back.views.log_in_view import LogInView
from back.views.sign_up_view import SignUpView
from django.urls import path


urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign-up"),
    path('login/', LogInView.as_view(), name='login')
]
