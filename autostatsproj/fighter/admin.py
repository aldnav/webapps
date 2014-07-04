from django.contrib import admin
from fighter.models import Fighter

# Register your models here.
class MatchInline(admin.TabularInline):
	model = Fighter
	fields = ('name', 'age', 'weight', 'height')

class FighterAdmin(admin.ModelAdmin):
	list_display = ('name', 'last_opponent', 'fight_status', 'pub_date')
	search_fields = ['name', 'age']
	fieldsets = [
		('Bio',			{'fields': ['name', 'age', 'weight', 'height']}),
		('Statistics', 	{'fields': ['division','wins','loses','draws','octagon_time','_540_metric', 'rating_points', 'win_finish', 'quality_performance','last_opponent','fight_status']})
	]

admin.site.register(Fighter, FighterAdmin)