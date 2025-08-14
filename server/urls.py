from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # or wherever you put it

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', include('accounts.urls')),
]
