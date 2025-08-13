from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome, you're signed up!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # ✅ Redirect target
    path('', include('accounts.urls')),
]
