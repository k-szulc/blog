from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import SignupForm

# Create your views here.

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('blogs:index'))

def register(request):
    """New user"""
    if request.method != 'POST':
        #Display the form
        form = SignupForm()
    else:
        #Process the form
        form = SignupForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user.groups.add(1)
            new_user.save()

            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
