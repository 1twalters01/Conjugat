from django.shortcuts import render, redirect
from .forms import HomeForm, SingleTestForm

# Create your views here.
def verb_test(request):
    if request.method == 'POST':
        pass
    else:
        return redirect('home')