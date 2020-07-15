import os
from django.shortcuts import render
from .models import Campaign
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from formtools.wizard.views import SessionWizardView



def test_function(request):
    return render(request, 'base.html',{})


class CampaignCreateView(SessionWizardView):
    template_name = 'business/campaign_create.html'
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'photos'))
    
    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        final = {}
        # New and awesome way of joining form data
        for data in form_data:
            final.update({**data})
        '''    
        print(final)
        # Old and less awesome way
        a = form_data[0]
        b = form_data[1]
        c = form_data[2]
        final = {**a,**b,**c}'''
        obj = Campaign(**final)
        obj.user = self.request.user
        obj.save()
        return render(self.request,'business/campaign_done.html', 
        {
            'form_data': [form.cleaned_data for form in form_list],
            'obj': obj,
        })


def my_campaign_list(request):
    campaigns = Campaign.objects.filter(user=request.user)
    context = {
        'campaigns': campaigns,
    }
    return render(request, 'business/campaign_list.html', context)