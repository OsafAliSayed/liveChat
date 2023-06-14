from django.db import models
from chat.models import *
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class UserGroup(models.Model):
    user = models.ForeignKey(User, related_name="usergroup", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="usergorup", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'group'], name='unique_migration_host_combination'
            )
        ]

    def __str__(self):
        return f"User: {self.user.username}, Group: {self.group.name}"
        
class Message(models.Model):
    group = models.ForeignKey(Group, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('datetime',)