from django.db import models

from django.contrib.auth import get_user_model

from django.conf import settings
from django.urls import reverse
import misaka

User=get_user_model()

from group.models import Group

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField()
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group,related_name='posts',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):

        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username,"pk":self.pk})
    class Meta():
        unique_together = ["user", "message"]
        ordering = ["-created_at"]


# Create your models here.
