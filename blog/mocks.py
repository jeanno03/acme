from django.http import Http404

class Posters():

	POSTERS=[
	{'id':1,'title':'Mon roi','body':'Livre du roi'},
	{'id':2,'title':'Ma Reine','body':'Livre de la Reine'},
	{'id':3,'title':'Mon Singe','body':'Livre du singe'},
	]

	@classmethod
	def all(cls):
		return cls.POSTERS

	@classmethod
	def find(cls, id):
		try:
			return cls.POSTERS[int(id)-1]
		except:
			print("Cela ne fonctionne pas j'avance")
			raise Http404('Sorry, error404, post #{} not found.'.format(id))
			raise Http500('Sorry, error500, post #{} not found.'.format(id))