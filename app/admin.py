from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import (
    Profile,
    Post,
    Attachment,
    Comment,
    Friendship
)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'modified_at',
        'status',
        'user',
        'text',
    )
    list_filter = ('created_at', 'modified_at', 'user')
    date_hierarchy = 'created_at'


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'modified_at',
        'status',
        'post',
        'file',
        'is_image',
    )
    list_filter = ('created_at', 'modified_at', 'post', 'is_image')
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text')
    list_filter = ('user', 'post')


@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'modified_at',
        'requester',
        'receiver',
        'status',
    )
    list_filter = ('created_at', 'modified_at', 'requester', 'receiver')
    date_hierarchy = 'created_at'

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)