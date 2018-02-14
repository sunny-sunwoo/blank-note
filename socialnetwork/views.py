# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.utils import timezone

from socialnetwork.forms import RegistrationForm, CreateForm, EditForm



@login_required
def search(request):
    if not 'last' in request.GET:
        return render(request, 'socialnetwork/search.html', {})

    last = request.GET['last']

    # Demonstrate one match case with Trump
    if last == 'jisup':
    	print("hi")
        context = { 'form': CreateForm() }
        return render(request, 'socialnetwork/profile.html', context)

    if last == 'sunny':
        context = { 'form': CreateForm() }
        return render(request, 'socialnetwork/profile2.html', context)

    if last == 'jeff':
        context = { 'form': CreateForm() }
        return render(request, 'socialnetwork/profile3.html', context)

    return render(request, 'socialnetwork/search.html', {'message': message})

@login_required
def create(request):
    if request.method == 'GET':
        context = { 'form': CreateForm() }
        return render(request, 'socialnetwork/create.html', context)

    create_form = CreateForm(request.POST)
    if not create_form.is_valid():
        context = { 'form': create_form }
        return render(request, 'socialnetwork/create.html', context)

    dummy_entry = { 'id': 1 }
    for field in [ 'last_name', 'first_name', 'birthday',
                'address', 'city', 'state', 'zip_code', 'country',
                'email', 'home_phone', 'cell_phone', 'fax',
                'spouse_last', 'spouse_first', 'spouse_birth', 'spouse_cell', 'spouse_email' ]:
        dummy_entry[field] = create_form.cleaned_data[field]

    dummy_entry['created_by']    = request.user
    dummy_entry['creation_time'] = timezone.now()
    dummy_entry['updated_by']    = request.user
    dummy_entry['update_time']  = timezone.now()

    # message = 'Entry created'
    # edit_form = EditForm(dummy_entry)
    # context = { 'message': message, 'entry': dummy_entry, 'form': edit_form }
    # return render(request, 'addrbook/edit.html', context)

@login_required
def profile(request):
    if request.method == 'GET':
        context = { 'form': CreateForm() }

        last = request.GET['last']
        # print(last)
    # Demonstrate one match case with Trump
    	if last == 'jisup':
    	    context = { 'form': CreateForm() }
    	    return render(request, 'socialnetwork/profile1.html', context)

    	elif last == 'sunny':
    	    context = { 'form': CreateForm() }
    	    return render(request, 'socialnetwork/profile2.html', context)

    	elif last == 'jeff':
    	    context = { 'form': CreateForm() }
    	    return render(request, 'socialnetwork/profile3.html', context)

    	else:
    		context = { 'form': CreateForm() }
    		return render(request, 'socialnetwork/profile.html', context)


	return render(request, 'socialnetwork/search.html', context)


@login_required
def following(request):
    if request.method == 'GET':
        context = { 'form': CreateForm() }
        return render(request, 'socialnetwork/following.html', context)


	return render(request, 'socialnetwork/search.html', context)


def register(request):
	context = {}

	# Just display the registration form if this is a GET request.
	if request.method == 'GET':
	    context['form'] = RegistrationForm()
	    return render(request, 'socialnetwork/register.html', context)

	# Creates a bound form from the request POST parameters and makes the 
	# form available in the request context dictionary.
	form = RegistrationForm(request.POST)
	context['form'] = form

	# Validates the form.
	if not form.is_valid():
	    return render(request, 'socialnetwork/register.html', context)

	# At this point, the form data is valid.  Register and login the user.
	new_user = User.objects.create_user(username=form.cleaned_data['username'], 
	                                    password=form.cleaned_data['password1'],
	                                    email=form.cleaned_data['email'],
	                                    first_name=form.cleaned_data['first_name'],
	                                    last_name=form.cleaned_data['last_name'])
	new_user.save()

	# Logs in the new user and redirects to his/her todo list
	new_user = authenticate(username=form.cleaned_data['username'],
	                        password=form.cleaned_data['password1'])
	login(request, new_user)
	return redirect(reverse('home'))