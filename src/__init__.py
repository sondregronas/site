"""Simple Pug rendering for Python"""
import os
import shutil

from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('.'),
    extensions=['pypugjs.ext.jinja.PyPugJSExtension']
)


def public_to_dist():
    """Copy contents of public to ../dist"""
    shutil.copytree('public', '../dist', dirs_exist_ok=True)


def write_html(template, pug_data, path='', dry_run=False):
    html = env.get_template(template).render(pug_data)

    if pug_data.get('url', ''):
        path = f"../dist/{pug_data['url']}.html"
    if not path:
        path = f"../dist/{template.replace('views/', '').replace('.pug', '.html')}"

    if not dry_run:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, 'wb').write(html.encode('utf-8'))
    return html
