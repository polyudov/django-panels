# coding: utf-8


from django.db import models
from django.contrib.auth.admin import Group
from distutils.core import setup_keywords


contexts = (
    ('p', 'primary'),
    ('s', 'success'),
    ('i', 'info'),
    ('w', 'warning'),
    ('d', 'danger'),
)


class Panel(models.Model):
    title = models.CharField(max_length=500, blank=True, verbose_name=u'Title')
    text = models.TextField(verbose_name=u'Text')

    visible = models.BooleanField(default=False, verbose_name=u'Visible for users')

    add_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    context = models.CharField(max_length=1, choices=contexts, default='i', verbose_name=u'Context',
                               help_text=u'Bootstrap class')

    urls_denorm = models.CharField(max_length=1000, blank=True, verbose_name=u'Visible on urls', help_text='/=home page, ')
    groups = models.ManyToManyField(Group, blank=True)

    def __unicode__(self):
        return self.text[:30]
