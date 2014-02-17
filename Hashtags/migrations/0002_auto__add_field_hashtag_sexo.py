# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Hashtag.sexo'
        db.add_column(u'Hashtags_hashtag', 'sexo',
                      self.gf('django.db.models.fields.CharField')(default='Masculino', max_length=150),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Hashtag.sexo'
        db.delete_column(u'Hashtags_hashtag', 'sexo')


    models = {
        u'Hashtags.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Hashtags']