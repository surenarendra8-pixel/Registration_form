from django.contrib import admin

from app1.models import Register

class Register_admin(admin.ModelAdmin):
    list_display = ['name','branch','college','place']

    list_filter = ['name']
    
admin.site.register(Register,Register_admin)


