'''
this contains routes related to user identity and authentication.
/user/registration/
/user/login/
/user/auth/
/user/logout/
'''
from django.urls import path
from users.views import registration_view, login_view
from users.views import auth_view, logout_view

urlpatterns = [
    path('registration/', registration_view, name = "registration"),
    path('login', login_view, name="login"),
    path('auth', auth_view, name="auth"),
    path('logout', logout_view, name="logout"),
]