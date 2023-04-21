from django.shortcuts import render, HttpResponsePermanentRedirect
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

#def login(request):
#    if request.method == "POST":
#        form = UserLoginForm(data=request.POST)
#        if form.is_valid():
#            username = request.POST["username"]
#            password = request.POST["password"]
#            user = auth.authenticate(username=username, password=password)
#            if user:
#                auth.login(request, user)
#                return HttpResponsePermanentRedirect(reverse('index'))
#    else:
#        form = UserLoginForm()
#    context = {"form": form}
#    return render(request, "users/sign_in.html", context)
#
#def registration(requset):
#    if requset.method == "POST":
#        form = UserRegistrationForm(data=requset.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponsePermanentRedirect(reverse('users:login'))
#    else:
#        form=UserRegistrationForm()
#    context = {"form": form}
#    return render(requset, "users/registration.html", context)



# то, что должно быть

from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        # получаем данные из запроса
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # проверяем, что пароли совпадают
        if password != confirm_password:
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match'})

        # проверяем, что пользователь с таким именем еще не зарегистрирован
        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'error', 'message': 'Username already exists'})

        # создаем нового пользователя
        user = User.objects.create_user(username=username, password=password)
        user.save()

        return JsonResponse({'status': 'success', 'message': 'User registered successfully'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        # получаем данные из запроса
        username = request.POST.get('username')
        password = request.POST.get('password')

        # аутентификация пользователя
        user = authenticate(request, username=username, password=password)

        # проверяем, что пользователь был успешно аутентифицирован
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'User logged in successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'})
