# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Fighter.fight_status'
        db.alter_column(u'fighter_fighter', 'fight_status', self.gf('django.db.models.fields.CharField')(max_length=5))

    def backwards(self, orm):

        # Changing field 'Fighter.fight_status'
        db.alter_column(u'fighter_fighter', 'fight_status', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            '_540_metric': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '200'}),
            'draws': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fight_status': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '5'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fighter.Fighter']", 'null': 'True'}),
            'loses': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'octagon_time': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 4, 0, 0)'}),
            'quality_performance': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'rating_points': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'win_finish': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['fighter']