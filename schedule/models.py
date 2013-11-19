from django.db import models

# Create your models here.


class swagCode(models.Model):
	code = models.CharField(max_length=100)
	worth = models.CharField(max_length=200)
	expires = models.DateTimeField()
	isActive = models.BooleanField(default=False)

	def __unicode__(self):
		return self.code
