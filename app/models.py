from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class BaseModel(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    DELETED = -1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (DELETED, 'Deleted')
    )
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=ACTIVE)

    class Meta:
        abstract = True

 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


class Attachment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    is_image = models.BooleanField()

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()