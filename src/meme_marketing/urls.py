from django.contrib import admin
from django.urls import path, include
from business.views import test_function
from users.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/', include('business.urls')),
    path('accounts/', include('allauth.urls')),
    path('', test_function),
]
