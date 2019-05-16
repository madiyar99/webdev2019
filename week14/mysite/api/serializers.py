from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import TaskList, Task

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id', 'username', 'email')


class TaskSerializer(serializers.ModelSerializer):
	id=serializers.IntegerField(read_only=True)
	tasklist_id=serializers.IntegerField(write_only=True)

	class Meta:
		model=Task
		fields=('id', 'name', 'status', 'tasklist_id')


class TaskSerializer2(serializers.ModelSerializer):
	id=serializers.IntegerField(read_only=True)

	class Meta:
		model=Task
		fields=('id', 'name', 'status')


class TaskListSerializer(serializers.ModelSerializer):
	id=serializers.IntegerField(read_only=True)
	created_by=UserSerializer(read_only=True)
	tasks=TaskSerializer2(many=True)

	class Meta:
		model=TaskList
		fields=('id', 'name', 'created_by', 'tasks')

	def create(self, validated_data):
		tasks=validated_data.pop('tasks')
		tasklist=TaskList.objects.create(**validated_data)

		for task in tasks:
			Task.objects.create(tasklist=tasklist, **task)
		return tasklist