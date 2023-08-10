"""
Admin registration for tags models
"""


from django.contrib import admin

from .models import TagAvailableValues, TagCategories


@admin.register(TagCategories)
class TagCategoriesAdmin(admin.ModelAdmin):
    """Admin for TagCategories"""
    search_fields = ('name', 'title')
    list_display = ('id', 'name', 'title')


@admin.register(TagAvailableValues)
class TagAvailableValuesAdmin(admin.ModelAdmin):
    """Admin for TagAvailableValues"""
    list_display = ('id', 'category', 'value')
