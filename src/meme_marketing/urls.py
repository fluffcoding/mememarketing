from django.contrib import admin
from django.urls import path, include
from business.views import test_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/', include('business.urls')),
    path('', test_function),
]
