from django.contrib import admin
from . models import Posts

@admin.register(Posts)
class PostsModelAdmin(admin.ModelAdmin):
    list_display=['author','content','title','Posted_Date']