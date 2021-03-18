from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_email(request):
    if request.method == 'POST':

        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect

    else:
        form = NameForm()

    return render(request, 'email_added.html', {'form': form})

def home(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'music.html')


def contact(request):
    return render(request, 'contact.html')
# Create your views here.
