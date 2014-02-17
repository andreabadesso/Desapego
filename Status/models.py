from django.db import models

class Status(models.Model):
	status = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.status

	class Meta:
		verbose_name = 'Status'
		verbose_name_plural = 'Status'

