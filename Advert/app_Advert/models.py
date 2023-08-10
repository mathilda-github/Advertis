from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.html import format_html

#from django.contrib.auth import get_user_model

# Create your models here.
'''
название
описание
торг
время создания
цена
время обновления


'''
#User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    descr = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг!')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%y')
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: orange; font-weight: bold;">Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d.%m.%y')


#    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
#    image = models.ImageField('изображение', upload_to='adverisements/')