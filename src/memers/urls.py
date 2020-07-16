from django.urls import path
from .views import active_campaigns_view, post_memes_for_campaign,delete_meme_view


urlpatterns = [
    path('active-campaigns/', active_campaigns_view, name='active-campaigns'),
    path('campaign/<id>/', post_memes_for_campaign, name='meme-submit'),
    path('meme/delete/<id>', delete_meme_view, name='delete-meme'),
]