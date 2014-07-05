# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fighter._540_metric'
        db.delete_column(u'fighter_fighter', '_540_metric')

        # Adding field 'Fighter.f_540_metric'
        db.add_column(u'fighter_fighter', 'f_540_metric',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Fighter._540_metric'
        db.add_column(u'fighter_fighter', '_540_metric',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Fighter.f_540_metric'
        db.delete_column(u'fighter_fighter', 'f_540_metric')


    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '200'}),
            'draws': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'f_540_metric': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fight_status': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '5', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fighter.Fighter']", 'null': 'True', 'blank': 'True'}),
            'loses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'octagon_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 5, 0, 0)'}),
            'quality_performance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating_points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'win_finish': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fighter']