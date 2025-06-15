from django.urls import path
from .views import login_user, registration_user, logout_user, profile_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', registration_user, name='register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile_user, name='profile'),
]
