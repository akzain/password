from django.urls import path, include
from password_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('password/', password, name="password"),
    path('about/', about, name="about")
]
