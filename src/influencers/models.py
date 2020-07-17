from django.db import models
from business.models import Campaign#, SM_SERVICES
from django.contrib.auth import get_user_model
from users.models import Profile
from memers.models import MemeImages

User = get_user_model()

SM_PLATFORMS = {
    ('f','facebook'),
    ('i','instagram'),
    ('t','twitter'),
    ('y','youtube'),
}


class CampaignExecutionUnit(models.Model):
    '''1. assigned_to_influencer
    2. campaign
    3. social_media_platform
    4. number_of_posts
    5. memes'''
    assigned_to_influencer = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    social_media_platform = models.CharField(choices=SM_PLATFORMS, max_length=50)
    number_of_posts = models.IntegerField()
    memes = models.ManyToManyField(MemeImages, blank=True)


class SocialMediaAsset(models.Model):
    profile = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    platform = models.CharField(max_length=20, choices=SM_PLATFORMS)
    permissions_granted = models.BooleanField(default=False)
    cpi = models.FloatField(null=True, blank=True)
