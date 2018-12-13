from cms.models.pluginmodel import CMSPlugin

from django.db import models

from djangocms_icon.fields import Icon
from filer.fields.image import FilerImageField

BG_IMAGE_POSITIONS = (
    ('', 'default'),
    ('center top', 'top'),
    ('center center', 'center'),
    ('center bottom', 'bottom'),
    ('left center', 'left'),
    ('right center', 'right'),
    ('left top', 'left top'),
    ('left bottom', 'left bottom'),
    ('right top', 'right top'),
    ('right bottom', 'right bottom'),
)

BG_IMAGE_SIZES = (
    ('auto', 'default'),
    ('cover', 'cover'),
    ('contain', 'contain'),
)

class CountersContainerModel(CMSPlugin):
    title = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(max_length=255, blank=True, null=True)
    bg_color = models.CharField(max_length=30, blank=True, null=True)
    bg_image = models.ImageField(upload_to='media/images', blank=True, null=True)
    bg_image_position = models.CharField(max_length=255, choices=BG_IMAGE_POSITIONS, blank=True, null=True)
    bg_image_size = models.CharField(max_length=255, choices=BG_IMAGE_SIZES, blank=True, null=True)
    button_text = models.CharField(max_length=255, blank=True, null=True)
    button_link = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title or 'counters container'

class CounterModel(CMSPlugin):
    counter_text = models.CharField(max_length=255, blank=True, null=True)
    counter_value = models.CharField(max_length=255, blank=True, null=True)
    icon = Icon(blank=False, default='fa-')
    image = FilerImageField(null=True, blank=True, related_name="title_image")

    def __unicode__(self):
        return self.counter_text or 'counter'
