from django.contrib import admin

from blog.models import Post
from comments.models import Comment
from profiles.models import Profile
from events.models import Event
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Event)


