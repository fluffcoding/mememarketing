from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from business.models import Campaign

from .models import Meme, MemeImages

from .forms import MemeSubmissionForm

@login_required
def active_campaigns_view(request):
    campaigns = Campaign.objects.filter(active=True)
    context = {
        'campaigns': campaigns,
    }
    return render(request, 'memers/active_campaigns.html', context)


@login_required
def post_memes_for_campaign(request, id):
    # Get campaign
    campaign = get_object_or_404(Campaign, id=id)
    # Create or get Meme under the campaign
    meme_object, created = Meme.objects.get_or_create(campaign=campaign,memer=request.user)
    # Obtain all previously uploaded images
    meme_images = meme_object.memerconnect.all()
    # Form for uploading new images
    meme_submit_form = MemeSubmissionForm(request.POST or None, request.FILES or None)
    if meme_submit_form.is_valid():
        parent_meme, created = Meme.objects.get_or_create(campaign=campaign,memer=request.user)
        image = meme_submit_form.cleaned_data['image']
        MemeImages.objects.create(parent_meme=parent_meme,image=image)
        
    context = {
        'campaign': campaign,
        'meme': meme_object,
        'meme_images': meme_images,
        'form': meme_submit_form,
    }
    return render(request, 'memers/post_memes_campaign.html', context)


@login_required
def delete_meme_view(request, id):
    meme_images = get_object_or_404(MemeImages, id=id)
    campaign = meme_images.parent_meme.campaign.id
    if meme_images.parent_meme.memer == request.user:
        meme_images.delete()
    return redirect(f'/memers/campaign/{campaign}' )
