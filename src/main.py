import os
from datetime import datetime

from __init__ import write_html, public_to_dist, get_clients_data, get_podcasts_data

BASE_URL = 'https://sondregronas.com'
SITE_NAME = 'Sondre Grønas'

PAGES = {
    'views/index.pug': {},
    'views/404.pug': {'title': '404 - Page not found',
                      'og_description': 'Page not found'},
    'views/clients.pug': {'title': f'Clients - {SITE_NAME}',
                          'clients': get_clients_data(),
                          'og_description': 'Meet our clients, are you next?'},
    'views/podcasts.pug': {'title': f'Podcasts - {SITE_NAME}',
                           'podcasts': get_podcasts_data(),
                           'og_description': 'Sondre Grønås has worked with a lot of podcasts, here are some of them.'},
    'views/old-content/managing-postgresql-on-a-synology-server.pug': {
        'title': 'Deprecated - Managing PostgreSQL on a Synology server',
        'url': 'managing-postgresql-on-a-synology-server',
        'og_description': 'Deprecated article - this article has been removed. Sorry for the inconvenience.'},
}

metadata = {
    'base_url': BASE_URL,
    'title_fallback': SITE_NAME,
    'og_image_fallback': f'{BASE_URL}/logo.png',
    'og_description_fallback': 'Sondre Grønås is a passionate ICT-educator and media engineer from Norway.',
    'year': datetime.now().year,
}

public_to_dist()
open('../dist/CNAME', 'w').write(BASE_URL.split('//')[1])
for page, data in PAGES.items():
    write_html(page, data | metadata)

os.system('npx tailwindcss -o ../dist/tailwind.min.css --minify')
