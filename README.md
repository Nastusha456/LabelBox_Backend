# LabelBox_Backend

classifier: .../<int:id>/classifier/<int:pk>/
# <int:id> - идентефикатор текущего пользователя
# <int:pk> - идентефикатор классификатора
response: json-объект классификатора 

annotation: .../<int:user_id>/annotation/<int:pk>
# <int:id> - идентефикатор текущего пользователя
# <int:pk> - идентефикатор аннотации
response: json-объект аннотации

registaration: .../users/register?format=json
# обмен данными при регистрации пользователя

login: .../users/login
# обмен данными при логине польщователя

change: .../users/change
# обмен данными при изменении имени пользователя или его почты 

response: для registaration. login и change присылается json- объект одного формата: {'status': ... , 'message': ... }, где status принимает одно из значений 'success' или 'error' в зависимости отого, успешно ли прошла регистрация. В случае ошибки также присылается 'message'в котором указывается возможная причина ошибки. 
=======
# Установка Django
pip install django==3.2.13

# Установка Django Rest framework
pip install djangorestframework

# установка Pillow
pip install Pillow
