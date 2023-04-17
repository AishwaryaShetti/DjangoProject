from django.contrib import admin
from . models import Pictures

@admin.register(Pictures)
class PostsModelAdmin(admin.ModelAdmin):
    list_display=['title','image']