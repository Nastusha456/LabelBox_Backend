from django.http import JsonResponse
from users.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json


@csrf_exempt
@api_view(['DELETE', 'GET', 'OPTIONS', 'PATCH', 'POST', 'PUT'])
def register(request):
    if request.method == 'POST':
        # получаем данные из запроса
        username = request.data.get('user_name')
        email = request.data.get("user_email")
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        # проверяем, что пользователь с таким именем еще не зарегистрирован
        if User.objects.filter(username=username).exists():
            return Response({'status': 'error', 'message': 'Username already exists'}, status=200)
        # создаем нового пользователя
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        # добавляем необходимые заголовки
        response = Response(
            {'status': 'success', 'message': 'User registered successfully'}, status=200, content_type='application/json')
        response['Access-Control-Allow-Origin'] = 'http://localhost:8081'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    else:
        print(3)
        return Response({'status': 'error', 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def Login(request):
    if request.method == 'POST':
        # получаем данные из запроса
        data = json.loads(request.body)
        print(data)
        username = data.get('user_name')
        password = data.get('password')
        #print("------------")
        #print(username, password)
        # аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        # проверяем, что пользователь был успешно аутентифицирован
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'User logged in successfully', "user_email": user.email})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'})
    

@csrf_exempt
def change(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'new_username' in data:
            usr = User.objects.get(username=data["user_name"])
            usr.username = data["new_username"]
            usr.save()
            return JsonResponse({'status': 'success', 'message': 'данные успешно изменены'})
        elif 'new_password' in data:
            usr = User.objects.get(username=data["user_name"])
            usr.password = data["new_password"]
            usr.save()
            return JsonResponse({'status': 'success', 'message': 'данные успешно изменены'})
        elif 'new_email' in data:
            usr = User.objects.get(username=data["user_name"])
            usr.email = data["new_email"]
            usr.save()
            return JsonResponse({'status': 'success', 'message': 'данные успешно изменены'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}) 

    # password for user_1 n4j5h2jk3b54jkh
    # password for user_2 54jk1h2jhk4vt / changed: changed_name 4h5j2j5jg2b5bj
    # test_user hv234hjvtfsn
    # test_user_2 hv234hjvtfsn