from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
	context = {
		'name': 'Student 1'
	}
	return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html')

def current_time(request):
	return HttpResponse('<h1>{}</h1>'.format(datetime.now()))

def show_product(request, pk):
	return HttpResponse('<h1>{}</h1>'.format(pk))

