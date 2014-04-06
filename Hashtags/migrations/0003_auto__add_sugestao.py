# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sugestao'
        db.create_table(u'Hashtags_sugestao', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Usuarios.Usuario'], null=True, blank=True)),
            ('fbId', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'Hashtags', ['Sugestao'])


    def backwards(self, orm):
        # Deleting model 'Sugestao'
        db.delete_table(u'Hashtags_sugestao')


    models = {
        u'Hashtags.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Hashtags.sugestao': {
            'Meta': {'object_name': 'Sugestao'},
            'fbId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Usuarios.Usuario']", 'null': 'True', 'blank': 'True'})
        },
        u'Usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['Usuarios.Usuario']", 'null': 'True', 'blank': 'True'}),
            'cadastrado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fbId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Hashtags']