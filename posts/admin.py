from django.contrib import admin
from website.posts.models import Post, StyleSheet, Script

class PostAdmin(admin.ModelAdmin):
   fieldsets = (
       (None, {
           'fields': (('title', 'slug', 'comments', 'public', 'information',), 'additional_header')
           #'fields': (('title', 'slug', 'comments', 'public', 'information', 'published', 'last_edited'), 'additional_header')
       }),
       ('Styles', {
           'classes': ('collapse',),
	   'fields': ('style_files', 'style')
       }),
       ('Scripts', {
           'classes': ('collapse',),
	   'fields': ('script_files', 'script')
       }),
       ('Body', {
           'fields': ('body',),
       }),
   )
   
   filter_horizontal = ('style_files', 'script_files')
   date_heirarchy = 'published'
   prepopulated_fields = {'slug': ('title',)}
   list_display = ('title', 'slug', 'comments', 'public', 'information', 'published', 'last_edited') 
   list_display_links = ('title',)
   list_filter = ('published', 'last_edited')
   list_editable = ['slug', 'comments', 'public', 'information']

   def save_model(self, request, obj, form, change):
      if not change:
         obj.author = request.user
      obj.save()

#class StyleSheetAdmin(admin.ModelAdmin):
#    pass

#class ScriptAdmin(admin.ModelAdmin):
#    pass

admin.site.register(Post, PostAdmin)
admin.site.register(StyleSheet)#, StyleSheetAdmin)
admin.site.register(Script)#, ScriptAdmin)
