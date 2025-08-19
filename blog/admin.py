from django.contrib import admin

# Register your models here.
from .models import AuthorModel,BlogModel,Tag

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","updated_at")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("fname","lname")

admin.site.register(AuthorModel,AuthorAdmin)
admin.site.register(BlogModel,BlogAdmin)
admin.site.register(Tag)