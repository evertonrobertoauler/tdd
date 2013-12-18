# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Articles.slug'
        db.add_column('app_articles', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True, default='v'),
                      keep_default=False)

        # Adding field 'Articles.created'
        db.add_column('app_articles', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Articles.slug'
        db.delete_column('app_articles', 'slug')

        # Deleting field 'Articles.created'
        db.delete_column('app_articles', 'created')


    models = {
        'app.articles': {
            'Meta': {'object_name': 'Articles'},
            'body': ('django.db.models.fields.TextField', [], {'default': "'q'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'default': "'v'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'default': "'y'"})
        }
    }

    complete_apps = ['app']