from django.shortcuts import render
from .models import CampaignExecutionUnit


def influencer_dashboard(request):
    campaign_execution_requests = CampaignExecutionUnit.objects.filter(assigned_to_influencer=request.user)
    context = {
        'campaigns': campaign_execution_requests,
    }
    return render(request, 'influencers/dashboard.html', context)


def single_campaign_execution(request, id):
    campaign_execution = CampaignExecutionUnit.objects.get(id=id)
    context = {
        'campaign': campaign_execution,
    }
    return render(request, 'influencers/single_campaign_execution.html', context)