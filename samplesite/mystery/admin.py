from django.contrib import admin
from .models import Rubric, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'context', 'rubric', 'published')
    list_display_links = ('title', 'context')
    search_fields = ('title', 'context')


admin.site.register(Rubric)
admin.site.register(Photo, PhotoAdmin)
