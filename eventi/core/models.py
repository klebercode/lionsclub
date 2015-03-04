# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _


STATE_CHOICES = (
    ('AC', u'Acre'),
    ('AL', u'Alagoas'),
    ('AP', u'Amapá'),
    ('AM', u'Amazonas'),
    ('BA', u'Bahia'),
    ('CE', u'Ceará'),
    ('DF', u'Distrito Federal'),
    ('ES', u'Espírito Santo'),
    ('GO', u'Goiás'),
    ('MA', u'Maranhão'),
    ('MT', u'Mato Grosso'),
    ('MS', u'Mato Grosso do Sul'),
    ('MG', u'Minas Gerais'),
    ('PA', u'Pará'),
    ('PB', u'Paraíba'),
    ('PR', u'Paraná'),
    ('PE', u'Pernambuco'),
    ('PI', u'Piauí'),
    ('RJ', u'Rio de Janeiro'),
    ('RN', u'Rio Grande do Norte'),
    ('RS', u'Rio Grande do Sul'),
    ('RO', u'Rondônia'),
    ('RR', u'Roraima'),
    ('SC', u'Santa Catarina'),
    ('SP', u'São Paulo'),
    ('SE', u'Sergipe'),
    ('TO', u'Tocantins'),
)


class Club(models.Model):
    name = models.CharField(_(u'Nome'), max_length=100)
    code = models.CharField(_(u'Distrito'), max_length=100,
                            blank=True, null=True)
    cnpj = models.CharField(_(u'CNPJ'), max_length=20,
                            help_text='99.999.999/9999-99',
                            blank=True, null=True)
    address = models.CharField(_(u'Endereço'), max_length=200,
                               blank=True, null=True)
    number = models.CharField(_(u'Número'), max_length=10,
                              blank=True, null=True)
    complement = models.CharField(_(u'Complemento'), max_length=100,
                                  blank=True, null=True)
    cep = models.CharField(_(u'CEP'), max_length=9, help_text='99999-999',
                           blank=True, null=True)
    district = models.CharField(_(u'Bairro'), max_length=100,
                                blank=True, null=True)
    city = models.CharField(_(u'Cidade'), max_length=100,
                            blank=True, null=True)
    state = models.CharField(_(u'UF'), max_length=2, choices=STATE_CHOICES,
                             blank=True, null=True)
    country = models.CharField(_(u'País'), max_length=50,
                               blank=True, null=True)
    phone1 = models.CharField(_(u'Fone 1'), max_length=20,
                              help_text='(99) 9999-9999',
                              blank=True, null=True)
    phone2 = models.CharField(_(u'Fone 2'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    phone3 = models.CharField(_(u'Fone 3 (Fax)'), max_length=20,
                              help_text='(99) 9999-9999', blank=True,
                              null=True)
    email = models.EmailField(_(u'Email'), blank=True, null=True)
    site = models.URLField(_(u'Site'), blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name = _(u'Clube')
        verbose_name_plural = _(u'Clubes')
        ordering = ['name']


class Info(models.Model):
    mesage = models.TextField(_(u'Informações do Evento'))

    def __unicode__(self):
        return unicode(self.pk)

    class Meta:
        verbose_name = _(u'Informação')
        verbose_name_plural = _(u'Informações')
        ordering = ['mesage']
