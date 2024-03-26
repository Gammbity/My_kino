from django.contrib import admin
from .models import CommentModel, FilmModel, AktyorModel

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']

@admin.register(FilmModel)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']

@admin.register(AktyorModel)
class AktyorAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']


