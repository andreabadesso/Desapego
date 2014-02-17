# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Amigo.amigo_rel'
        db.add_column(u'Amigos_amigo', 'amigo_rel',
                      self.gf('django.db.models.fields.CharField')(default='100000502532875', max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Amigo.amigo_rel'
        db.delete_column(u'Amigos_amigo', 'amigo_rel')


    models = {
        u'Amigos.amigo': {
            'Meta': {'object_name': 'Amigo'},
            'amigo_rel': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Amigos']