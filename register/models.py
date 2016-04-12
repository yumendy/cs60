from __future__ import unicode_literals

from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField


class Record(models.Model):
    name = models.CharField(max_length=256)
    graduate = models.SmallIntegerField()
    unit = models.CharField(max_length=512)
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    im = models.CharField(max_length=32, null=True, blank=True)
    wechat = models.CharField(max_length=32, null=True, blank=True)
    short_word = models.CharField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)

    def __unicode__(self):
        return self.name + ':' + self.short_word
