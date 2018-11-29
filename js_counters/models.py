from cms.models.pluginmodel import CMSPlugin

from django.db import models

class CountersContainerModel(CMSPlugin):
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(max_length=255, blank=True, null=True)
    bg_image = models.ImageField(upload_to='media/images', blank=True, null=True)
    button_text = models.CharField(max_length=255, blank=True, null=True)
    button_link = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title

class CounterModel(CMSPlugin):
    counter_text = models.CharField(max_length=255, blank=True, null=True)
    counter_value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title
