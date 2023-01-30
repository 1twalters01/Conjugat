from .forms import InfoForm, EmailForm
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import hashlib
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError



''' Mailchimp ping '''
mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})

#Check if mailchimp is working
def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)



''' Subscribe'''
def request_reset(request):
    request.session['email'] = None
    return None

def does_email_exist(request):
    email = None
    if request.user.is_authenticated:
        try:
            email = User.objects.get(username=request.user).email
        except:
            email = None
    if not email:
        email = request.session.get('email', None)
    return email


def create_member(cd, email):
    member_info = {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': cd['first_name'],
                'LNAME': cd['last_name'],
            }
        }
    if cd['languages']:
        member_info['tags'] = cd['languages']
    return member_info


def subscribe(request):
    email = does_email_exist(request)
    if email:
        if request.method == 'POST':
            if request.POST.get('new-email'):
                email = request_reset(request)
                return redirect('newsletter:subscribe')

            try:
                form = InfoForm(request.POST, initial='test')
                if form.is_valid() == False:
                    return HttpResponse('invalid form')

                cd = form.cleaned_data
                member_info = create_member(cd, email)
                mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                return render(request, 'newsletter/success.html')
                
            except ApiClientError as error:
                return HttpResponse(error.text)

        else:
            form = InfoForm()
            context = {'form':form}
        return render(request, 'newsletter/info.html', context)

    else:
        if request.method == 'POST':
            form = EmailForm(request.POST, initial='test')
            if form.is_valid() == False:
                    return HttpResponse('invalid form')
            cd = form.cleaned_data
            request.session['email'] = cd['email']
            return redirect('newsletter:subscribe')
        else:
            form = EmailForm()
            context = {'form':form}
        return render(request, 'newsletter/email.html', context)


''' Unsubscribe '''
def unsubscribe(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, initial='test')
        if form.is_valid():
            try:
                cd = form.cleaned_data
                email_hash = hashlib.md5(cd['email'].encode('utf-8').lower()).hexdigest()
                member_update = {'status': 'unsubscribed',}
                response = mailchimp.lists.update_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    email_hash,
                    member_update,
                )
                context = {'unsubscribe':True}
                return render(request, 'newsletter/success.html', context)
            except ApiClientError as error:
                return HttpResponse(error.text)
    else:
        form = EmailForm()
        context = {'form':form}
    return render(request, 'newsletter/unsubscribe.html', context)