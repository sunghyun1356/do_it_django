from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()


    head_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)

    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_dile_Exit(self):
        return self.get_file_name().split('.')[-1]