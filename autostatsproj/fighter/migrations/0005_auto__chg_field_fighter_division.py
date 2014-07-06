# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Fighter.division'
        db.alter_column(u'fighter_fighter', 'division', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Fighter.division'
        db.alter_column(u'fighter_fighter', 'division', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'draws': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'f_540_metric': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'fight_status': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '5', 'null': 'True'}),
            'fm_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'last_opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fighter.Fighter']", 'null': 'True', 'blank': 'True'}),
            'loses': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'mma_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'octagon_time': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 6, 0, 0)'}),
            'quality_performance': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'rating_points': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'win_finish': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        }
    }

    complete_apps = ['fighter']