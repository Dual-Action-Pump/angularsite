from . import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        uf = forms.UserForm(request.POST)
        if uf.is_valid():
            user = User.objects.create_user(username=uf.cleaned_data['username'],
                                            email=uf.cleaned_data['email'],
                                            password=uf.cleaned_data['password'])
            user2 = authenticate(username=uf.cleaned_data['username'], password=uf.cleaned_data['password'])
            login(request, user2)
            return HttpResponseRedirect("/")
    else:
        uf = forms.UserForm()
    return render_to_response('registration/register.html',  dict(userform=uf,), context_instance=RequestContext(request))
