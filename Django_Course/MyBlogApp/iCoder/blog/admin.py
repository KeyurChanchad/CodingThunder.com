from django.contrib import admin
from .models import Post, BlogComment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('comment',)
    search_fields = ('user',)
    list_per_page = 4

# Register your models here.
admin.site.register(BlogComment)

@admin.register(Post) # This is for when you want to register model and change admin panel

class PostAdmin(admin.ModelAdmin): 
    class Media:
        js= ('tinyInject.js',)
    