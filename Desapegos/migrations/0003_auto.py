# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field amigos on 'Desapego'
        db.delete_table(db.shorten_name(u'Desapegos_desapego_amigos'))


    def backwards(self, orm):
        # Adding M2M table for field amigos on 'Desapego'
        m2m_table_name = db.shorten_name(u'Desapegos_desapego_amigos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('desapego', models.ForeignKey(orm[u'Desapegos.desapego'], null=False)),
            ('usuario', models.ForeignKey(orm[u'Usuarios.usuario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['desapego_id', 'usuario_id'])


    models = {
        u'Desapegos.desapego': {
            'Meta': {'object_name': 'Desapego'},
            'alvo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desapegados'", 'to': u"orm['Usuarios.Usuario']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['Hashtags.Hashtag']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '150', 'null': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '150', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Status.Status']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desapegos'", 'to': u"orm['Usuarios.Usuario']"})
        },
        u'Hashtags.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Status.status': {
            'Meta': {'object_name': 'Status'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'desapego'", 'symmetrical': 'False', 'to': u"orm['Usuarios.Usuario']"}),
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

    complete_apps = ['Desapegos']