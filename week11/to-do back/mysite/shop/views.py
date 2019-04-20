from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from shop.models import Category
# Create your views here.

def index(request):
	count = Category.objects.count()
	categories = Category.objects.all()
	json_categories = [c.to_json() for c in categories]
	data = {
		'category_count': json_categories,
		#'nums': [a for a in range(10)]
	}
	return JsonResponse(data, safe=False)