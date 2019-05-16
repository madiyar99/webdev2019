from django.db import models
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TaskList(models.Model):
	name=models.CharField(max_length=200)
	created_by=models.ForeignKey(User, on_delete=models.CASCADE, 
		default=None, null=True)

	class  Meta:
		verbose_name='TaskList'
		verbose_name_plural='TaskLists'

	def __str__(self):
		return '{}:{}'.format(self.name, self.created_by)

	def to_json(self):
		return {
			'name':self.name,
			'created by':self.created_by
		}

class Task(models.Model):
	name=models.CharField(max_length=200)
	status=models.CharField(max_length=200)
	created_at=models.DateTimeField(auto_now=True)
	tasklist=models.ForeignKey(TaskList, 
		on_delete=models.CASCADE, 
		related_name='tasks')

	class  Meta:
		verbose_name='Task'
		verbose_name_plural='Tasks'

	def __str__(self):
		return '{}:{}'.format(self.name, self.status)

	def to_json(self):
		return {
			'name':self.name,
			'status':self.status
		}