# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _
from django.utils import timezone

from eventi.receipts.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscription', 'created_at',
                    'subscribed_today',)
    date_hierarchy = 'created_at'
    search_fields = ('name', 'subscription', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        print "%s = %s = %s" % (obj.created_at,
                                datetime.today().date(),
                                timezone.now().date())
        return obj.created_at == datetime.today().date()

    subscribed_today.short_description = _(u'Enviado hoje?')
    subscribed_today.boolean = True


admin.site.register(Receipt, ReceiptAdmin)
