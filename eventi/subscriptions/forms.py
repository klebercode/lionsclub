# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

from eventi.subscriptions.models import Subscription


def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números.'))
    if len(value) != 11:
        raise ValidationError(_(u'CPF deve ter 11 números.'))


class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if not value:
            return [None, None]
        return value.split('-')


class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField(),
                  forms.IntegerField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if not data_list:
            return ''
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido'))
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido.'))
        return '%s-%s' % tuple(data_list)


class SubscriptionForm(forms.ModelForm):
    # phone = PhoneField(label=_('Telefone'), required=False)
    extra = forms.CharField(label=_(u'Local e Data'), required=False,
                            widget=forms.TextInput(
                            attrs={'placeholder': 'Cidade, Data'}))

    class Meta:
        model = Subscription
        exclude = ('paid', 'cpf')

    # def __init__(self, *args, **kwargs):
    #     super(SubscriptionForm, self).__init__(*args, **kwargs)

    #     self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = map(lambda w: w.capitalize(), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
                not self.cleaned_data.get('phone'):
            raise ValidationError(_(u'Informe seu e-mail ou telefone.'))

        return self.cleaned_data

    def send_mail(self, pk):
        subject = u'Lions Clubes, inscrição realizada.'
        context = {
            'name': self.cleaned_data['name'],
            'phone': self.cleaned_data['phone'],
            'email': self.cleaned_data['email'],
            'subscription': pk,
        }

        email_to = self.cleaned_data['email']
        message = render_to_string('subscriptions/subscribe_mail.txt', context)
        message_html = render_to_string('subscriptions/subscribe_mail.html',
                                        context)
        msg = EmailMultiAlternatives(subject, message,
                                     'convencao@lionsclubegaranhuns.org.br',
                                     [email_to])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
