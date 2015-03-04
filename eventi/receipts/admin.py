# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from django.utils import timezone

from eventi.receipts.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscription', 'created_at', 'get_attach',
                    'subscribed_today',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'subscription', 'created_at')
    list_filter = ['created_at']

    def get_attach(self, obj):
        return '<a href="%s" target="_Blank">Baixar</a><br>' % obj.attach.url

    get_attach.short_description = _(u'Comprovante')
    get_attach.allow_tags = True

    def subscribed_today(self, obj):
        try:
            created = obj.created_at.date()
        except:
            created = obj.created_at

        print "%s = %s = %s" % (created,
                                datetime.today(),
                                timezone.now())
        return created == datetime.today().date()

    subscribed_today.short_description = _(u'Enviado hoje?')
    subscribed_today.boolean = True


admin.site.register(Receipt, ReceiptAdmin)
