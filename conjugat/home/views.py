from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from verbs.forms import HomeForm

@login_required
def home(request):
    form = HomeForm()
    context = {'section':'home', request: request, 'form':form}
    return render(request,'home/home.html',context)

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context = {}
        return render(request, 'home/landing_page.html',context)

def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

def faq(request):
    context = {}
    return render(request, 'home/faq.html', context)

def privacy(request):
    context = {}
    return render(request, 'home/privacy.html', context)

def terms(request):
    context = {}
    return render(request, 'home/terms.html', context)