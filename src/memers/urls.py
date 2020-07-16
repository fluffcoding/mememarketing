from django.urls import path
from .views import active_campaigns_view, post_memes_for_campaign


urlpatterns = [
    path('active-campaigns/', active_campaigns_view, name='active-campaigns'),
    path('campaign/<id>/', post_memes_for_campaign)
]