# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Articles'
        db.create_table('app_articles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140, default='j')),
            ('body', self.gf('django.db.models.fields.TextField')(default='y')),
        ))
        db.send_create_signal('app', ['Articles'])


    def backwards(self, orm):
        # Deleting model 'Articles'
        db.delete_table('app_articles')


    models = {
        'app.articles': {
            'Meta': {'object_name': 'Articles'},
            'body': ('django.db.models.fields.TextField', [], {'default': "'y'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'j'"})
        }
    }

    complete_apps = ['app']