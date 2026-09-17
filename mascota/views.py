from django.shortcuts import render


def mascota(request):
	"""Muestra el perfil principal de la mascota."""
	return render(request, 'perfil.html')


def perfil(request):
	"""Muestra el perfil de la mascota."""
	return render(request, 'perfil.html')


def galeria(request):
	"""Muestra la galería de fotos de la mascota."""
	return render(request, 'galeria.html')
