from django.contrib import admin
from .models import User, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "likeCount", "created_time")


# Register your models here.
admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
