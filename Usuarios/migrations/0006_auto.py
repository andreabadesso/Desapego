# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field amiguinhos on 'Usuario'
        db.delete_table(db.shorten_name(u'Usuarios_usuario_amiguinhos'))

        # Adding M2M table for field amigos on 'Usuario'
        m2m_table_name = db.shorten_name(u'Usuarios_usuario_amigos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_usuario', models.ForeignKey(orm[u'Usuarios.usuario'], null=False)),
            ('to_usuario', models.ForeignKey(orm[u'Usuarios.usuario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_usuario_id', 'to_usuario_id'])


    def backwards(self, orm):
        # Adding M2M table for field amiguinhos on 'Usuario'
        m2m_table_name = db.shorten_name(u'Usuarios_usuario_amiguinhos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('usuario', models.ForeignKey(orm[u'Usuarios.usuario'], null=False)),
            ('amigo', models.ForeignKey(orm[u'Amigos.amigo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['usuario_id', 'amigo_id'])

        # Removing M2M table for field amigos on 'Usuario'
        db.delete_table(db.shorten_name(u'Usuarios_usuario_amigos'))


    models = {
        u'Usuarios.usuario': {
            'Meta': {'object_name': 'Usuario'},
            'amigos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['Usuarios.Usuario']", 'null': 'True', 'blank': 'True'}),
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

    complete_apps = ['Usuarios']