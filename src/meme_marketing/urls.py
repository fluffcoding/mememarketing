from django.contrib import admin
from django.urls import path, include
from business.views import test_function
from users.views import profile_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('business/', include('business.urls')),
    path('accounts/', include('allauth.urls')),
    path('memers/', include('memers.urls')),
    path('influencers/',include('influencers.urls')),
    path('', test_function),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)