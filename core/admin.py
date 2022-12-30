from django.contrib import admin
from .models import Category, Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "writer", "updated", "created")
    prepopulated_fields = {"slug": ("title",)}


class CategoroyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "updated", "created")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoroyAdmin)
admin.site.register(Blog, BlogAdmin)
