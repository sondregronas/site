from csv import DictReader
from dataclasses import dataclass


@dataclass
class Client:
    name: str
    role: str
    logo: str
    project: str
    url: str


CLIENTS = [Client(name=row['name'],
                  role=row['role'],
                  logo=row['logo'],
                  project=row['project'],
                  url=row['url'])
           for row in DictReader(open('clients.csv', 'r', encoding='utf-8'))]