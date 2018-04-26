from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time', 'modified_time', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)