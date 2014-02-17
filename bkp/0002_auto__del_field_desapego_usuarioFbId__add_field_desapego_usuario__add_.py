# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Desapego.usuarioFbId'
        db.delete_column(u'Desapegos_desapego', 'usuarioFbId')

        # Adding field 'Desapego.usuario'
        db.add_column(u'Desapegos_desapego', 'usuario',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='2312', related_name='desapegos', to=orm['Usuarios.Usuario']),
                      keep_default=False)

        # Adding field 'Desapego.alvo'
        db.add_column(u'Desapegos_desapego', 'alvo',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='23123', related_name='desapegados', to=orm['Usuarios.Usuario']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Desapego.usuarioFbId'
        db.add_column(u'Desapegos_desapego', 'usuarioFbId',
                      self.gf('django.db.models.fields.CharField')(default='12031', max_length=150),
                      keep_default=False)

        # Deleting field 'Desapego.usuario'
        db.delete_column(u'Desapegos_desapego', 'usuario_id')

        # Deleting field 'Desapego.alvo'
        db.delete_column(u'Desapegos_desapego', 'alvo_id')


    models = {
        u'Desapegos.desapego': {
            'Meta': {'object_name': 'Desapego'},
            'alvo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desapegados'", 'to': u"orm['Usuarios.Usuario']"}),
            'alvoFbId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Hashtags.Hashtag']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Status.Status']"}),
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