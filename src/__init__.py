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
