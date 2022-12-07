from django.urls import path  
from . import views  #из этой же директории импорт файла views

urlpatterns = [
    path('', views.index , name ='home'), 
    path('my menu', views.menu , name = 'menu'), 
    path ("your register", views.register, name= 'register'),
]