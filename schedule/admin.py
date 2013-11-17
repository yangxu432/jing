from django.contrib import admin
from schedule.models import swagCode
# Register your models here.
class swagCodeAdmin(admin.ModelAdmin):
	list_display = ('code','worth','expires','isActive')
	list_filter = ('worth',)
	ordering = ('-id',)
admin.site.register(swagCode, swagCodeAdmin)