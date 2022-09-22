#место где хранятся модели приложения, модели это инструкции для формирования данных в бд
from django.db import models
#здесб будем описывать таблицу бд для наших приложений и это делается только для одного приложения

# Create your models here.

class Order(models.Model): #который наследует клас моделей тот что испортирован выше для БДшки
    order_dt = models.DateTimeField(auto_now=True) #дата создания
    order_name = models.CharField(max_length=200, verbose_name='Имя') #verbose_name='Имя' показывает на сайте как отображается это
    order_phone = models.CharField(max_length=200, verbose_name='Телефон') #как создали модель теперь нужно сделать миграцию python manage.py makemigrations

    def __str__(self):
        return self.order_name #возвращает вмесето order имена в бд

    class Meta:
        verbose_name = 'Заказ' #меняет значение класса order на имя заказ зы
        verbose_name_plural = 'Заказы'





