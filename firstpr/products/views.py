from django.shortcuts import render , HttpResponse

# Create your views here.
# переменные - контролеры - вьюхи

def index (request):
    context = {
        'title' : 'home' ,
        'is_promo': True, #если True то элемент в этом блоке html виден пользователю
        'title' : 'menu',
        'menu' : [
            {
                'name' : 'паста',
                'structure' : 'курица грибы',
            },
            {
                'name' : 'суп',
                'structure' : 'вода картошка',
            },
        ]
         }
    return render (request , 'products/index.html', context)

def menu (request):
    return render (request , 'products/menu.html')

def register (request):
    return render (request , 'products/register.html')
