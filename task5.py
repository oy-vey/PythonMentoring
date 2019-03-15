from bs4 import BeautifulSoup

def get_links(html):
    url_list = []
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        url_list.append(link.get('href'))
    return url_list