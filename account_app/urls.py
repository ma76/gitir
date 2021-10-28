from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', Login,name = 'login'),
    path('register', Register,name = 'login'),
    path('logout',log_out)
]
