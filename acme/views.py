#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#return HttpResponse('<h1>Hello Acme</h1>')
	return render(request, 'home.html')

def about(request):
	return render(request, 'pages/about.html')

def about(request):
	return render(request, 'pages/contact.html')