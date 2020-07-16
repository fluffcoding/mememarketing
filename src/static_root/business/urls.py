from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CampaignCreateView, my_campaign_list, single_campaign
from .forms import CampaignForm, ServiceTypes, ContentForm
from django.contrib.auth.decorators import login_required


app_name= 'business'

urlpatterns = [
    path('create/', login_required(CampaignCreateView.as_view([CampaignForm, ServiceTypes, ContentForm])), name='create-campaign'),
    path('campaigns/', my_campaign_list, name='my-campaigns'),
    path('campaign/<id>', single_campaign, name='single-campaign'),
]
