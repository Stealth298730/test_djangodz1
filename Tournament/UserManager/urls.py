from django.urls import path
from .views import sign_in, sign_up, logout_func

urlpatterns = [
    path("sign_in/", sign_in, name="sign_in"),
    path("sign_up/", sign_up, name="sign_up"),
    path("logout/", logout_func, name="logout"),
]
