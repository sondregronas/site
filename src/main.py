import os
from datetime import datetime

from __init__ import write_html, public_to_dist
from clients import CLIENTS

pages = {
    'views/index.pug': {},
    'views/clients.pug': {'clients': CLIENTS},
}

metadata = {
    'title': 'Sondre Grønås',
    'favicon': 'favicon.ico',
    'description': 'Sondre Grønås is a passionate ICT-educator and media engineer from Norway.',
    'year': datetime.now().year,
}

public_to_dist()
for page, data in pages.items():
    write_html(page, data | metadata)

os.system('npx tailwindcss -o ../dist/tailwind.min.css --minify')
