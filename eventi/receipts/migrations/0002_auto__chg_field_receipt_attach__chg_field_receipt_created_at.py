# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Receipt.attach'
        db.alter_column(u'receipts_receipt', 'attach', self.gf('django.db.models.fields.files.FileField')(default=0, max_length=100))

        # Changing field 'Receipt.created_at'
        db.alter_column(u'receipts_receipt', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Receipt.attach'
        db.alter_column(u'receipts_receipt', 'attach', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True))

        # Changing field 'Receipt.created_at'
        db.alter_column(u'receipts_receipt', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    models = {
        u'receipts.receipt': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Receipt'},
            'attach': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 3, 3, 22, 27, 5, 1)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subscription': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['receipts']