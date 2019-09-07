from django.contrib import admin
from thingsdone.models import ThingDone, Day, Week, Month

# Register your models here.
class DayAdmin(admin.ModelAdmin):
  list_display = ('day','user',)
  list_filter = ('user',)
  
class MonthAdmin(admin.ModelAdmin):
  list_display = ('start_day','user',)
  list_filter = ('user',)

class WeekAdmin(admin.ModelAdmin):
  list_display = ('start_day','user',)
  list_filter = ('user',)
  
class ThingDoneAdmin(admin.ModelAdmin):
  list_display = ('name', 'day', 'month', 'week', 'owner')
  list_filter = ('day', 'month', 'week', 'owner')
  
admin.site.register(ThingDone, ThingDoneAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Week, WeekAdmin)
admin.site.register(Month, MonthAdmin)