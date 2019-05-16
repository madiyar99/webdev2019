from django_filters import rest_framework as filters
from api.models import Task

class TaskFilter(filters.FilterSet):
	name=filters.CharFilter(lookup_exp='contains')
	status=filters.CharFilter(lookup_exp='contains')

	class Meta:
		model=Task
		fields=('name','status')