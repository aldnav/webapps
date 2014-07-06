from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200, null=True, blank=True)
    fm_url = models.CharField(max_length=200, null=True, blank=True)
    mma_url = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(editable=True, null=True,blank=True)
    age = models.IntegerField(null=True, default=0)
    weight = models.IntegerField('Weight (lbs)',null=True, default=0)
    height = models.IntegerField('Height (inches)',null=True, default=0)
    wins = models.IntegerField(null=True, default=0)
    loses = models.IntegerField(null=True, default=0)
    draws = models.IntegerField(null=True, default=0)
    octagon_time = models.IntegerField('Octagon Time (mins)',null=True, default=0)
    f_540_metric = models.IntegerField('540 Metric',null=True, default=0)
    rating_points = models.IntegerField('Rating Points',null=True, default=0)
    win_finish = models.IntegerField('Win Finish %',null=True, default=0)
    quality_performance = models.IntegerField('Quality Performance %',null=True, default=0)
    divisions = (
        ('WW', 'welterweight'),
        ('LW', 'lightweight'),
        ('MW', 'middleweight')
    )
    division = models.CharField(max_length=200, choices=divisions, default='WW', null=True, blank=True)
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