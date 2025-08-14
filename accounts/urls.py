from django.urls import path
from .views import signup_view

urlpatterns = [
    path('', signup_view, name='home'),         # root URL now shows the signup form
    path('signup/', signup_view, name='signup') # optional: keep this if you want both
]
