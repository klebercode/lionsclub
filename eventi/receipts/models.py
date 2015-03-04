# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Receipt(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    subscription = models.IntegerField(_(u'Número de Inscrição'))
    attach = models.FileField(_(u'Selecione um arquivo'),
                              upload_to='documents/%Y/%m/%d')
    created_at = models.DateTimeField(_(u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Comprovante')
        verbose_name_plural = _(u'Comprovantes')
        ordering = ['-created_at']
