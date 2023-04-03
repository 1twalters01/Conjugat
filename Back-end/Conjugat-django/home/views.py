from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from verbs.forms import HomeForm

@login_required
def home(request):
    form = HomeForm()
    context = {'section':'home', request: request, 'form':form}
    return render(request,'home/home.html',context)