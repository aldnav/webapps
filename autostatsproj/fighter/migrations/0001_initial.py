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
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('loses', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('draws', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('octagon_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_540_metric', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rating_points', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('win_finish', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('quality_performance', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('division', self.gf('django.db.models.fields.CharField')(default='WW', max_length=200)),
            ('last_opponent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fighter.Fighter'], null=True, blank=True)),
            ('fight_status', self.gf('django.db.models.fields.CharField')(default='W', max_length=5, null=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 4, 0, 0))),
        ))
        db.send_create_signal(u'fighter', ['Fighter'])


    def backwards(self, orm):
        # Deleting model 'Fighter'
        db.delete_table(u'fighter_fighter')


    models = {
        u'fighter.fighter': {
            'Meta': {'object_name': 'Fighter'},
            '_540_metric': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'division': ('django.db.models.fields.CharField', [], {'default': "'WW'", 'max_length': '200'}),
            'draws': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fight_status': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '5', 'null': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_opponent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fighter.Fighter']", 'null': 'True', 'blank': 'True'}),
            'loses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'octagon_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 7, 4, 0, 0)'}),
            'quality_performance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating_points': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'win_finish': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fighter']