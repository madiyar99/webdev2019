from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from api.serializers import TaskListSerializer, TaskSerializer
from api.models import TaskList, Task

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from api.filters import TaskFilter

class ListTaskLists(generics.ListCreateAPIView):
	serializer_class=TaskListSerializer
	permission_classes=(IsAuthenticated, )

	def get_queryset(self):
		return TaskList.objects.filter(created_by=self.request.user)

	def perform_create(self, serializer):
		serializer.save(created_by=self.request.user)


class SelectedTaskList(generics.RetrieveUpdateDestroyAPIView):
	queryset=TaskList.objects.all()
	serializer_class=TaskListSerializer
	filterset_fields=('name', 'status')

class Tasks(generics.ListCreateAPIView):
	serializer_class=TaskSerializer
	pagination_class = LimitOffsetPagination
	filter_backends=(DjangoFilterBackend,
					filters.SearchFilter,
					filters.OrderingFilter)

	#Django filter
	filter_class=TaskFilter

	#filterset_fields=('name', 'status'), only for exact

	#SearchFilter
	search_fields=('name', 'status')

	#Ordering Filter
	ordering_fields=('name', 'status')
	ordering=('name')


