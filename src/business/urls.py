from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CampaignCreateView
from .forms import CampaignForm, ServiceTypes, ContentForm

app_name= 'business'

urlpatterns = [
    path('create/', CampaignCreateView.as_view([CampaignForm, ServiceTypes, ContentForm]), name='create-campaign'),
]
