# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Fighter.weight'
        db.add_column(u'fighter_fighter', 'weight',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.height'
        db.add_column(u'fighter_fighter', 'height',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.wins'
        db.add_column(u'fighter_fighter', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.loses'
        db.add_column(u'fighter_fighter', 'loses',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.draws'
        db.add_column(u'fighter_fighter', 'draws',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.octagon_time'
        db.add_column(u'fighter_fighter', 'octagon_time',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter._540_metric'
        db.add_column(u'fighter_fighter', '_540_metric',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.rating_points'
        db.add_column(u'fighter_fighter', 'rating_points',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.win_finish'
        db.add_column(u'fighter_fighter', 'win_finish',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.quality_performance'
        db.add_column(u'fighter_fighter', 'quality_performance',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Fighter.division'
        db.add_column(u'fighter_fighter', 'division',
                      self.gf('django.db.models.fields.CharField')(default='WW', max_length=200),
                      keep_default=False)

        # Adding field 'Fighter.fight_status'
        db.add_column(u'fighter_fighter', 'fight_status',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


        # Changing field 'Fighter.age'
        db.alter_column(u'fighter_fighter', 'age', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Fighter.weight'
        db.delete_column(u'fighter_fighter', 'weight')

        # Deleting field 'Fighter.height'
        db.delete_column(u'fighter_fighter', 'height')

        # Deleting field 'Fighter.wins'
        db.delete_column(u'fighter_fighter', 'wins')

        # Deleting field 'Fighter.loses'
        db.delete_column(u'fighter_fighter', 'loses')

        # Deleting field 'Fighter.draws'
        db.delete_column(u'fighter_fighter', 'draws')

        # Deleting field 'Fighter.octagon_time'
        db.delete_column(u'fighter_fighter', 'octagon_time')

        # Deleting field 'Fighter._540_metric'
        db.delete_column(u'fighter_fighter', '_540_metric')

        # Deleting field 'Fighter.rating_points'
        db.delete_column(u'fighter_fighter', 'rating_points')

        # Deleting field 'Fighter.win_finish'
        db.delete_column(u'fighter_fighter', 'win_finish')

        # Deleting field 'Fighter.quality_performance'
        db.delete_column(u'fighter_fighter', 'quality_performance')

        # Deleting field 'Fighter.division'
        db.delete_column(u'fighter_fighter', 'division')

        # Deleting field 'Fighter.fight_status'
        db.delete_column(u'fighter_fighter', 'fight_status')


        # User chose to not deal with backwards NULL issues for 'Fighter.age'
        raise RuntimeError("Cannot reverse this migration. 'Fighter.age' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Fighter.age'
        db.alter_column(u'fighter_fighter', 'age', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            '_540_metric': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '200'}),
            'draws': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'fight_status': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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