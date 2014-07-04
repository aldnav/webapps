from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=True, null=True,blank=True)
    age = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField('Weight (lbs)',null=True,blank=True)
    height = models.IntegerField('Height (inches)',null=True,blank=True)
    wins = models.IntegerField(null=True,blank=True)
    loses = models.IntegerField(null=True,blank=True)
    draws = models.IntegerField(null=True,blank=True)
    octagon_time = models.IntegerField('Octagon Time (mins)',null=True,blank=True)
    _540_metric = models.IntegerField('540 Metric',null=True,blank=True)
    rating_points = models.IntegerField('Rating Points',null=True,blank=True)
    win_finish = models.IntegerField('Win Finish %',null=True,blank=True)
    quality_performance = models.IntegerField('Quality Performance %',null=True,blank=True)
    divisions = (
        ('WW', 'welterweight'),
        ('LW', 'lightweight'),
        ('MW', 'middleweight')
    )
    division = models.CharField(max_length=200, choices=divisions, default='WW')
    last_opponent = models.ForeignKey('self', null=True,blank=True)
    fight_status_options = (
        ('W', 'win'),
        ('L', 'loss'),
        ('D', 'draw')
    )
    fight_status = models.CharField(max_length=5, choices=fight_status_options, default='W', null=True,)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Fighter, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('fighter_detail', (self.slug,self.id))