# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from eventi.core.models import Club


USAGE_CHOICES = (
    (1, 'CL'),
    (2, 'CaL'),
    (3, 'DM'),
    (4, 'LEO'),
)


class Subscription(models.Model):
    club = models.ForeignKey(Club, verbose_name=_(u'Clube'))
    usage = models.IntegerField(_(u'Tratamento'), choices=USAGE_CHOICES,
                                default=1)
    name = models.CharField(_(u'Nome'), max_length=100)
    cpf = models.CharField(_(u'CPF'), max_length=11, unique=True,
                           blank=True, null=True)
    birth = models.DateField(_(u'Data de Nascimento'), blank=True, null=True,
                             help_text=_(u'Para Premiação'))
    leo = models.DateField(_(u'Data de Ingresso no Leonísmo'), blank=True,
                           null=True, help_text=_(u'Para Premiação'))
    job_club = models.CharField(_(u'Cargo no Clube'), max_length=100,
                                blank=True, null=True,)
    job_dist = models.CharField(_(u'Cargo no Distrito'), max_length=100,
                                blank=True, null=True,)
    job_mult = models.CharField(_(u'Cargo no Distrito Múltiplo'),
                                max_length=100, blank=True, null=True,)
    phone = models.CharField(_(u'Telefone'), max_length=20)
    email = models.EmailField(_(u'Email'))
    hotel = models.CharField(_(u'Hotel de Hospedagem'), max_length=100,
                             blank=True, null=True)
    extra = models.CharField(_(u'Cidade, Data'), max_length=150,
                             blank=True, null=True)
    created_at = models.DateField(_(u'Criado em'), auto_now_add=True)
    paid = models.BooleanField(_(u'Pago'), default=False)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
        ordering = ['-created_at']
