from django.contrib import admin
from players.models import Player, SellHistory, Sell, Team


admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Sell)
admin.site.register(SellHistory)

# @admin.register(Player)
# class PlayerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'owner')
