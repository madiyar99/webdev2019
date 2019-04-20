from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 200)

	def __str__(self):
		return '{} :{}'.format(self.id, self.name)

	def to_json(self):
		return {
			'id': self.id,
			'name': self.name
		}