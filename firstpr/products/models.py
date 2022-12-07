from django.db import models
# from firstpr.wsgi import *

# Create your models here.
# models = таблицы
# ./manage.py makemigretion -для миграции всех конструкции


# модель категорий:
class category (models.Model):
    name = models.CharField(max_length=128)  #CharField - это строковое поле для строк малого и большого размера (максимум указываем сами)
    description = models.TextField(null=True,blank=True) #ну понятно что то для бол кол-во текста (поле может быть пустым)

class eat (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField ()
    price = models.DecimalField (max_digits=6, decimal_places=2)#для работы с ценами (сколько цифр до и после запятой)
    quantity = models.PositiveIntegerField(default=0) #кол-во товаров (по умолчанию)
    # image = models.ImageField(upload_to='product_images')для изображений (куда будут сохранятся изображения)
    category = models.ForeignKey(to=category, on_delete=models.CASCADE)#к какой категории относится продукт (связываем нашу модель с другим классом, cascade - предупреждает об удалении всего в категории  protect - не удалит пока категория не будет пустой )

class fok (models.Model):
    name = models.CharField(max_length=30)
    dea = models.TextField()
