import models
from django.contrib import admin

class StaticPageAdmin(admin.ModelAdmin):
    fields = ('slug', 'body')
    
admin.site.register(models.StaticPage, StaticPageAdmin)
