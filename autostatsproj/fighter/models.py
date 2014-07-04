from django.db import models
from django.utils import timezone

# Create your models here.
class Fighter(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField()
	pub_date = models.DateTimeField('date published', default=timezone.now())