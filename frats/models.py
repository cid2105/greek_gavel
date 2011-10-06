from django.db import models

class Frat(models.Model):
 	university = models.ForeignKey('unis.University')
	name = models.CharField(max_length=200)
	date = models.DateTimeField('date added')
 
	def __unicode__(self):
		return self.name
