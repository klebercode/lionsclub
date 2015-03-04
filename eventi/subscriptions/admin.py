# coding: utf-8
from django.contrib import admin
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, ugettext as _

from eventi.subscriptions.models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at',
                    'subscribed_today', 'paid')
    list_display_links = ('id', 'name')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'created_at')
    list_filter = ['created_at', 'paid']

    def subscribed_today(self, obj):
        try:
            created = obj.created_at.date()
        except:
            created = obj.created_at

        return created == datetime.today().date()

    subscribed_today.short_description = _(u'Inscrito hoje?')
    subscribed_today.boolean = True

    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%d inscrição foi marcada como paga.',
            u'%d inscrições foram marcadas como pagas.',
            count
        )
        self.message_user(request, msg % count)

    mark_as_paid.short_description = _('Marcar como pago')


admin.site.register(Subscription, SubscriptionAdmin)
