from django.shortcuts import render

def index(request):
    return render(request, "lablebox/index.html") #"create-vue-app/src/pages/Main.vue")
