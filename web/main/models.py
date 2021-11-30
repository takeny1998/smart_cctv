from django.db import models

# Create your models here.
class Event(models.Model):

	datetime = models.DateTimeField()
	video = models.FileField(blank=True, upload_to="videos/")

	def __str__(self):
		return f"Motion Event #{self.id}"