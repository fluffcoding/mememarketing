from django.urls import path

from .views import influencer_dashboard, single_campaign_execution

urlpatterns = [
    path('dashboard/', influencer_dashboard, name='influencer-dashboard'),
    path('single_campaign/<id>/', single_campaign_execution, name='single-execution')
]
