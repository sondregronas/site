import os
from datetime import datetime

from __init__ import write_html, public_to_dist, get_clients_data

BASE_URL = 'https://sondregronas.github.io/sondregronas.com'
SITE_NAME = 'Sondre Grønas'

PAGES = {
    'views/index.pug': {},
    'views/404.pug': {'title': '404 - Page not found',
                      'og_description': 'Page not found'},
    'views/clients.pug': {'title': f'Clients - {SITE_NAME}',
                          'clients': get_clients_data(),
                          'og_description': 'Meet our clients, are you next?'},
}

metadata = {
    'base_url': BASE_URL,
    'title_fallback': SITE_NAME,
    'og_image_fallback': f'{BASE_URL}/logo.png',
    'og_description_fallback': 'Sondre Grønås is a passionate ICT-educator and media engineer from Norway.',
    'year': datetime.now().year,
}

public_to_dist()
for page, data in PAGES.items():
    write_html(page, data | metadata)

os.system('npx tailwindcss -o ../dist/tailwind.min.css --minify')
