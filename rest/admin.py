from django.contrib import admin
from .models import Rest
# Register your models here.
class RestAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Rest._meta.fields]
	list_editable=("no","rest")
admin.site.register(Rest,RestAdmin)