import os
from datetime import datetime

from __init__ import write_html, public_to_dist, CLIENTS

pages = {
    'views/index.pug': {},
    'views/clients.pug': {'clients': CLIENTS,
                          'og_description': 'Meet our clients, are you next?'},
}

metadata = {
    'title': 'Sondre Grønås',
    'og_description_fallback': 'Sondre Grønås is a passionate ICT-educator and media engineer from Norway.',
    'og_image_fallback': 'logo.png',
    'year': datetime.now().year,
}

public_to_dist()
for page, data in pages.items():
    write_html(page, data | metadata)

os.system('npx tailwindcss -o ../dist/tailwind.min.css --minify')
