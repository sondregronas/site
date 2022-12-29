"""Simple Pug rendering for Python"""
import os
import shutil
from csv import DictReader

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'),
    extensions=['pypugjs.ext.jinja.PyPugJSExtension']
)


def public_to_dist() -> None:
    """Copy contents of public to ../dist"""
    shutil.copytree('public', '../dist', dirs_exist_ok=True)


def write_html(template: str, pug_data: dict, path: str = '', dry_run: bool = False) -> str:
    html = env.get_template(template).render(pug_data)

    if pug_data.get('url', ''):
        path = f"../dist/{pug_data['url']}.html"
    if not path:
        path = f"../dist/{template.replace('views/', '').replace('.pug', '.html')}"

    if not dry_run:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'wb').write(html.encode('utf-8'))
    return html


def get_clients_data() -> list[dict]:
    return [{'name': row['name'],
             'role': row['role'],
             'logo': row['logo'],
             'project': row['project'],
             'url': row['url']}
            for row in DictReader(open('clients.csv', 'r', encoding='utf-8'))]


def get_podcasts_data() -> list[dict]:
    return [{'name': row['name'],
             'logo': row['logo'],
             'url': row['url']}
            for row in DictReader(open('podcasts.csv', 'r', encoding='utf-8'))]


def generate_sitemap(base_url: str) -> None:
    """Generate sitemap.xml"""
    pages = [base_url] + [f'{base_url}/{page.split(".html")[0]}'
                          for page in os.listdir('../dist')
                          if page.endswith('.html') and page not in ['404.html', 'index.html']]

    pages_xml = '\n'.join([f'\t<url>\n\t\t<loc>{page}</loc>\n\t</url>' for page in pages])
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n' \
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' \
              f'{pages_xml}\n' \
              '</urlset>'

    open('../dist/sitemap.xml', 'w').write(sitemap)
