from datetime import datetime

from __init__ import *

BASE_URL = 'https://sondregronas.com'
SITE_NAME = 'Sondre Grønas'
DEV_MODE = os.path.exists('../dist')  # use path.exists for now to check if in dev mode, removes analytics

PAGES = {
    'views/index.pug': {},
    # 404 page
    'views/404.pug': {'title': '404 - Page not found',
                      'og_description': 'Page not found'},
    # clients
    'views/clients.pug': {'title': f'Clients - {SITE_NAME}',
                          'clients': get_clients_data(),
                          'og_description': 'Meet our clients, are you next?'},
    # podcasts
    'views/podcasts.pug': {'title': f'Podcasts - {SITE_NAME}',
                           'podcasts': get_podcasts_data(),
                           'og_description': 'Sondre Grønås has worked with a lot of podcasts, here are some of them.'},
    # Legacy articles - might be removed in the future
    'views/legacy/managing-postgresql-on-a-synology-server.pug': {
        'title': 'Deprecated - Managing PostgreSQL on a Synology server',
        'url': 'managing-postgresql-on-a-synology-server',
        'og_description': 'Deprecated article - the article contents have been removed. '
                          'Sorry for the inconvenience. I recommend you check out this docker container by '
                          'Elliot Mason instead, as it\'s a better solution than the one I wrote about here: '
                          'https://github.com/elliotmatson/Docker-Davinci-Resolve-Project-Server'},
}

metadata = {
    'base_url': BASE_URL,
    'title_fallback': SITE_NAME,
    'og_image_fallback': f'{BASE_URL}/logo.png',
    'og_description_fallback': 'Sondre Grønås is a passionate ICT-educator and media engineer from Norway.',
    'year': datetime.now().year,
    'dev': DEV_MODE,
}

public_to_dist()
open('../dist/CNAME', 'w').write(BASE_URL.split('//')[1])
for page, data in PAGES.items():
    write_html(page, data | metadata)
generate_sitemap(BASE_URL)
minimize_dist()

os.system('npx tailwindcss -o ../dist/tailwind.min.css --minify')
