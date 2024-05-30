from django.contrib import admin

from blog.models import Post
from comments.models import Comment
from profiles.models import Profile
from events.models import Event
# Register your models here.

class ApiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')

admin.site.register(Post, ApiAdmin)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Event)


# 