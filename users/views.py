from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


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
            new_user.is_active = False
            new_user.save()

            current_site = get_current_site(request)
            mail_subject = "Activate your Sqn's blog account."
            message = render_to_string('users/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': new_user.pk,
                'token': account_activation_token.make_token(new_user),

            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponseRedirect(reverse('blogs:index'))

            #return HttpResponse('Please confirm your email address to complete the registration')



    context = {'form': form}
    return render(request, 'users/register.html', context)

def activate(request, pk, token):
    try:
        uid = pk
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('blogs:index'))
    else:
        return HttpResponse('Activation link is invalid!')
