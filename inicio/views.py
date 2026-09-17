from django.http import Http404
from django.shortcuts import render


# Datos: no se utiliza una base de datos para esta actividad.
CATEGORIAS = {
    'artistas': {
        'titulo': 'Artistas Favoritos',
        'icono': '🎤',
        'descripcion': 'Una de las frases que más me gusta es: "Taylor Swift tiene una cancion para todo" y siempre ha sido asi',
        'historia': 'Es la artista de pop mas escuchada internacionalmente y con una gran trayectoria musical, que ha marcado a varias generaciones con sus canciones y su estilo único.',
        'campo_1_nombre': 'Canción favorita',
        'campo_1': 'All Too Well (Taylor\'s Version)',
        'campo_2_nombre': 'Álbum favorito',
        'campo_2': 'Red (Taylor\'s Version)',
    },
    'series': {
        'titulo': 'Series Favoritas',
        'icono': '📺',
        'descripcion': 'Series que me mantienen entretenido y con ganas de ver más.',
        'historia': 'Es uno de los K-dramas que ha enganchado a muchos nuevos expectadores occidentales y que ha sido un éxito en la plataforma de streaming Netflix.',
        'campo_1_nombre': 'Mi serie favorita',
        'campo_1': 'Propuesta laboral ( 사내 맞선)',
        'campo_2_nombre': 'Género favorito',
        'campo_2': 'Romanace y comedia',
    },
    'mascota': {
        'titulo': 'Mis Mascota',
        'icono': '🐾',
        'descripcion': 'Mi más pequeña amiga de cuatro patas',
        'historia': 'Mi comapñera de adolecente y parte de mi joven adultez',
        'campo_1_nombre': 'Edad',
        'campo_1': '7 años',
        'campo_2_nombre': 'Especie',
        'campo_2': 'Gata',
        
        
    },
    'libros': {
        'titulo': 'Libros Favoritos',
        'icono': '📚',
        'descripcion': 'Un libro con un mensaje profundo.',
        'historia': 'Es una novela que narra la vida de Evelyn Hugo, una actriz ficticia de Hollywood, y su ascenso a la fama, sus amores y secretos a lo largo de varias décadas.',
        'campo_1_nombre': 'Libro destacado',
        'campo_1': 'Los Siete maridos de Evelyn Hugo',
        'campo_2_nombre': 'Género favorito',
        'campo_2': 'Romance y drama',
        'campo_3_nombre': 'Autora favorita',
        'campo_3': 'Taylor Jenkins Reid',
        
    },
}


def inicio(request):
    """Muestra el menú principal de categorías."""
    return render(request, 'inicio/inicio.html')


def detalle(request, categoria):
    """Muestra los datos de una categoría o devuelve un error 404."""
    datos = CATEGORIAS.get(categoria)

    if datos is None:
        raise Http404('La categoría solicitada no existe.')

    return render(request, 'inicio/detalle.html', {
        'categoria': categoria,
        'datos': datos,
    })
