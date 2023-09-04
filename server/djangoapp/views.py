from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

def get_contacts(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contacts.html', context)

def get_aboutus(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

def get_user_logged_in(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
        return username

def get_logout(request):
    logout(request)
    return redirect('/djangoapp')

def get_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/djangoapp")  # Use 'return' to perform the redirection
        else:
            # Return an 'invalid login' error message.
            # You can render a template or return an HttpResponse here.
            # For example:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        # Handle GET request, e.g., rendering the login form.
        # You can render your login template here.
        return render(request, 'login.html')
    
def get_registration_view(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
    
def add_new_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)  # Log in the user
            return redirect("/djangoapp/new_user_success")  # Redirect to a success page
        else:
            # Passwords do not match; you can handle this error as needed.
            error_message = "Passwords do not match"
            return render(request, 'registration.html', {'error_message': error_message})

    return render(request, 'registration.html')

def get_new_user_success_view(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/new_user_success.html', context)
# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

