from django.contrib import admin

from gateau.models import Dessert, Cafe, Review, Video


@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    pass


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ["pk", "dessert", "name", "scenery_image", "address"]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ["cafe", "title", "youtube_link"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
