#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	#return HttpResponse('<h1>Hello Acme</h1>')
	return render(request, 'home.html')

def about(request):
	return render(request, 'pages/about.html')

def contact(request):
	return render(request, 'pages/contact.html')

def handler404(request, exception):
	return render(request, 'errors/404.html', {'error':exception}, status=404)
#	return render(request, 'errors/404.html', {}, status=404)

def handler500(request, exception=None):
	return render(request, 'errors/500.html', {'error':exception}, status=500)