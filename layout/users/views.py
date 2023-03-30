from django.shortcuts import render, HttpResponsePermanentRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {"form": form}
    return render(request, "users/sign_in.html", context)

def registration(requset):
    if requset.method == "POST":
        form = UserRegistrationForm(data=requset.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('users:login'))
    else:
        form=UserRegistrationForm()
    context = {"form": form}
    return render(requset, "users/registration.html", context)

#def index(request):
#    context = {
#        "title": 'some shit'
#    }
#    return render(request, "users/index.html", context)