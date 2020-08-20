from django.shortcuts import render
from .forms import MemberForm

# Create your views here.


def register(request):
	""" This function does something ..."""

	# Construire le formulaire, soit avec les données postées,
	# soit vide si l'utilisateur accède pour la première fois
	# à la page.

	form = MemberForm(request.POST or None)
	# Nous vérifions que les données envoyées sont valides
	# Cette méthode renvoie False s'il n'y a pas de données 
	# dans le formulaire ou qu'il contient des erreurs.
	if form.is_valid(): 
		# Ici nous pouvons traiter les données reçues du formulaire
		firstname = form.cleaned_data['firstname']
		lastname = form.cleaned_data['lastname']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		context = {
			'lastname' :	lastname,
		}
		return render(request, 'member/register.html', context)
		# Nous pourrions ici envoyer l'e-mail grâce aux données 
		# que nous venons de récupérer
		envoi = True
	# Quoiqu'il arrive, on affiche la page du formulaire.
	return render(request, 'member/register.html', locals())
	#return render(request, 'member/register.html')
