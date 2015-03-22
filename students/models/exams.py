# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Exam(models.Model):
    """Exam Model"""

    class Meta(object):
        verbose_name = u"Іспит"
        verbose_name_plural = u"Іспити"

    exam_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Предмет")

    exam_day = models.DateField(
        blank=False,
        verbose_name=u"Дата проведення",
        null=True)

    teacher_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")

    exam_group = models.ForeignKey('Group',
        verbose_name=u'Група',
        blank=False,
        null=True,
        on_delete=models.PROTECT)
    
    def __unicode__(self):
        return u"%s %s" % (self.exam_name, self.teacher_name)



