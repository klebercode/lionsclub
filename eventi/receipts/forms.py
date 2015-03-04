# coding: utf-8
from django import forms
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from eventi.receipts.models import Receipt
from eventi.subscriptions.models import Subscription


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt

    def send_mail(self):
        subject = u'Lions Clubes, comprovante enviado.'
        context = {
            'name': self.cleaned_data['name'],
            'subscription': self.cleaned_data['subscription'],
        }

        s = Subscription.objects.get(pk=self.cleaned_data['subscription'])
        if s:
            email_to = s.email
        else:
            email_to = ''

        message = render_to_string('receipts/receipt_mail.txt', context)
        message_html = render_to_string('receipts/receipt_mail.html',
                                        context)
        msg = EmailMultiAlternatives(subject, message,
                                     'no-reply@lionsclubegaranhuns.org.br',
                                     [email_to])

        msg.attach_alternative(message_html, 'text/html')
        msg.send()
