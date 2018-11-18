from django.shortcuts import render

from .mocks import Posters

#posters=[
#	{'id':1,'title':'Mon roi','body':'Livre du roi'},
#	{'id':2,'title':'Ma Reine','body':'Livre de la Reine'},
#	{'id':3,'title':'Mon Singe','body':'Livre du singe'},
#]

# Create your views here.
def index(request):
	posts=['First Post', 'Second Post', 'Third Post']
	return render(request, 'blog/index.html', {'toto': posts})

def toto(request):
	posterVide=[]
	posters=Posters.all()
	return render(request, 'blog/toto.html', {'posterEnvoye':posters, 'posterVide':posterVide})

def show(request, id):
	posters=Posters.find(id)
	return render(request, 'blog/show.html',{'post':posters})
