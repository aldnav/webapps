# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fighter'
        db.create_table(u'fighter_fighter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 4, 0, 0))),
        ))
        db.send_create_signal(u'fighter', ['Fighter'])


    def backwards(self, orm):
        # Deleting model 'Fighter'
        db.delete_table(u'fighter_fighter')


    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 4, 0, 0)'})
        }
    }

    complete_apps = ['fighter']