
from django.db import models
from utils.choices import Country
from django.contrib.auth.models import User



class player(models.Model):
	class Meta:
		verbose_name = "Игроки"
		verbose_name_plural = 'Игроки'
		ordering = ('year', )
	year = models.CharField(verbose_name="возраст", max_length=40)
	country = models.CharField(max_length=50, choices=Country.choices, default=Country.KAZ, verbose_name="Страна")
	owner = models.IntegerField(verbose_name="id владельца", default=0)
	coast = models.IntegerField(default=100000, verbose_name="цена")
	power = models.IntegerField(default=1, verbose_name="сила")
	name = models.CharField(max_length=50, verbose_name="Название", null=True)

	def __str__(self):
		return f'{self.name}'

