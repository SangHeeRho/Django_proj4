from django.contrib import admin

from gateau.models import Dessert, Cafe, Video, Recipe


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    pass


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ["pk", "dessert", "name", "scenery", "address"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "youtube_link"]


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
