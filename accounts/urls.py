from django.urls import path
from .views import signup_view

urlpatterns = [
    path('', signup_view, name='home'),  # Root URL shows signup form
]
