from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from friendship.models import Friend, Follow, Block

from .models import (
    Profile,
    Post,
    Attachment,
    Comment
)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    extras = 1

class AttachmentInline(admin.StackedInline):
    model = Attachment
    verbose_name_plural = 'Attachments'
    fk_name = 'post'



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
    inlines = (AttachmentInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text')
    list_filter = ('user', 'post')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)