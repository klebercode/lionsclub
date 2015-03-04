# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Receipt'
        db.create_table(u'receipts_receipt', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('subscription', self.gf('django.db.models.fields.IntegerField')()),
            ('attach', self.gf('filebrowser.fields.FileBrowseField')(max_length=200, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'receipts', ['Receipt'])


    def backwards(self, orm):
        # Deleting model 'Receipt'
        db.delete_table(u'receipts_receipt')


    models = {
        u'receipts.receipt': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Receipt'},
            'attach': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subscription': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['receipts']