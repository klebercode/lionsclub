# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Receipt.created_at'
        db.alter_column(u'receipts_receipt', 'created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Receipt.created_at'
        db.alter_column(u'receipts_receipt', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        u'receipts.receipt': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Receipt'},
            'attach': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subscription': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['receipts']