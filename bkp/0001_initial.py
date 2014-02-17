# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Desapego'
        db.create_table(u'Desapegos_desapego', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuarioFbId', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('alvoFbId', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Status.Status'])),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'Desapegos', ['Desapego'])

        # Adding M2M table for field hashtags on 'Desapego'
        m2m_table_name = db.shorten_name(u'Desapegos_desapego_hashtags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('desapego', models.ForeignKey(orm[u'Desapegos.desapego'], null=False)),
            ('hashtag', models.ForeignKey(orm[u'Hashtags.hashtag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['desapego_id', 'hashtag_id'])


    def backwards(self, orm):
        # Deleting model 'Desapego'
        db.delete_table(u'Desapegos_desapego')

        # Removing M2M table for field hashtags on 'Desapego'
        db.delete_table(db.shorten_name(u'Desapegos_desapego_hashtags'))


    models = {
        u'Desapegos.desapego': {
            'Meta': {'object_name': 'Desapego'},
            'alvoFbId': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hashtags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['Hashtags.Hashtag']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Status.Status']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'usuarioFbId': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'Hashtags.hashtag': {
            'Meta': {'object_name': 'Hashtag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'Status.status': {
            'Meta': {'object_name': 'Status'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Desapegos']