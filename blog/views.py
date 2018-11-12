from django.shortcuts import render

# Create your views here.
def index(request):
	posts=['First Post', 'Second Post', 'Third Post']
	return render(request, 'blog/index.html', {'toto': posts})

def toto(request):
	posters=[
		{'id':1,'title':'Mon roi','body':'Livre du roi'},
		{'id':2,'title':'Ma Reine','body':'Livre de la Reine'},
		{'id':3,'title':'Mon Singe','body':'Livre du singe'},
	]

	posterVide=[]
	return render(request, 'blog/toto.html', {'posterEnvoye':posters, 'posterVide':posterVide})
