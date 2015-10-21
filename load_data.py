#!/usr/bin/python
from __future__ import (
    unicode_literals,
    print_function,
    absolute_import,
)
import json
import code
import pprint
import requests

with open('index.json') as fd:
    d = json.load(fd)

apps = d['apps']

def for_github_apps(f=lambda x: print(x), apps=apps):
    for app in apps:
        if app.get('codeLink', '').startswith('https://github.com'):
            f(app)

def github_url_has_issues_working(app_data):
    url = app_data['codeLink']

    if url.endswith('/'):
        url = url[:-1]

    assert not url.endswith('/')

    issueslink = url + '/issues'

    response = requests.get(issueslink, allow_redirects=False)
    if response.status_code == 200:
        return True
    else:
        print('Got', response.status_code, 'for', issueslink,
              'with location header', repr(response.headers.get('location', '')))
        return False

code.interact(local=locals())
