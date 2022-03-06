from datetime import datetime

from django.db import models

import readtime
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField()
    featured_image = models.ImageField(upload_to='posts/')
    full_description = RichTextUploadingField(config_name='greenshop_ckeditor')
    created_at = models.DateTimeField(default=datetime.now)

    def get_readtime(self):
        result = readtime.of_html(self.full_description)
        return result.text

    def __str__(self):
        return self.title
