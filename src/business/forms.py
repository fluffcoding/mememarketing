from django import forms

from .models import Campaign

class CampaignForm(forms.ModelForm):
    min_budget = 10000
    advertising_budget = forms.IntegerField(min_value=min_budget, help_text='Please specify your advertising budget in PKR. Minimum advertising budget is '+str(min_budget)+' PKR')
    class Meta:
        model = Campaign
        fields = ('title','advertising_budget',)


class ServiceTypes(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('services',)


class ContentForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ('description',)