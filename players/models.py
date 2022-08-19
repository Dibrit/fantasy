from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from utils.choices import Country, Role
from django.contrib.auth.models import User
from regist.models import User
from django.conf import settings
from utils import constants

class Team(models.Model):
    money = models.IntegerField(default=10000000)
    # power = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    country = models.CharField(choices=Country.choices, default=Country.KAZ, verbose_name="Страна", max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class Player(models.Model):
	class Meta:
		verbose_name = "Игроки"
		verbose_name_plural = 'Игроки'
		ordering = ('year', )
	year = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(40)])
	country = models.CharField(choices=Country.choices, default=Country.KAZ, verbose_name="Страна", max_length=20)
	# power = models.IntegerField(default=1, verbose_name="сила")
	role = models.CharField(choices=Role.choices, verbose_name="тип игрока", max_length=20)
	last_name = models.CharField(verbose_name="Имя", max_length=20)
	first_name = models.CharField(verbose_name="Фамилилия", max_length=20)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)

	def update_price(self, new_team_country):
		self.market_value *= self.get_price_raise_due_to_age()
		self.market_value *= self.get_price_raise_due_to_position()
		self.market_value *= self.get_price_raise_for_domestic_player(new_team_country)

	def get_price_raise_due_to_age(self):
		if self.age <= constants.YOUNGEST_PLAYER_AGE:
			return constants.PRICE_RAISE_FOR_YOUNGEST_PLAYERS
		if self.age <= constants.YOUNG_PLAYER_AGE:
			return constants.PRICE_RAISE_FOR_YOUNG_PLAYERS
		return 1

	def get_price_raise_due_to_position(self):
		return constants.PRICE_RAISE_DEPENDING_ON_POSITION[self.position]

	def get_price_raise_for_domestic_player(self, new_team_country):
		if self.country == new_team_country:
			return constants.PRICE_RAISE_FOR_DOMESTIC_PLAYER
		return 1

	def __str__(self):
		return f"{self.first_name} {self.last_name} / {self.country}"


class Sell(models.Model):
	player = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
	coast = models.IntegerField(verbose_name="цена")
	sold = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.player.first_name} {self.player.last_name} / {self.coast}"


class SellHistory(models.Model):
	sold_time = models.DateTimeField(auto_now_add=True, verbose_name="время покупки")
	selling_team = selling_team = models.ForeignKey(
        Team, on_delete=models.DO_NOTHING, related_name="sales"
    )
	buying_team = models.ForeignKey(
        Team, on_delete=models.DO_NOTHING, related_name="purchases"
    )
	transfer = models.ForeignKey(Sell, on_delete=models.DO_NOTHING)

	def __str__(self):
		return f"{self.transfer} / {self.sold_time}"


# class GameHistory(models.Model):
# 	team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
# 	game_time = models.DateTimeField(auto_now_add=True, verbose_name="время игры")
# 	won = models.BooleanField()
#
# 	def __str__(self):
# 		return f"{self.game_time} / {self.team}"