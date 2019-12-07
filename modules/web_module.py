from requests import get, post
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import re

def simple_get(url):
    """
    poskusi dobiti vsebino na url-ju z HTTP GET requestom
    Če je vsebina urlja HTML ali XML, vrnemo text, drugeče None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
           and content_type is not None 
           and content_type.find('html') > -1)


def log_error(e):
    '''
    Vedno je dobra ideja error log. 
    Ta funkcija samo sprinta napako.
    '''
    print(e)

def ih_web_scrap(wiki_link):
    
    #webLink = "https://wiki.razor.si/index.php?title=Special:AllPages"
    webLink = f"{wiki_link}/index.php?title=Special:AllPages"
    
    raw_html = simple_get(webLink)
    soup = BeautifulSoup(raw_html, 'html.parser')
    
    pages = []
    
    for ultag in soup.find_all('ul', {'class': 'mw-allpages-chunk'}):
        for litag in ultag.find_all('li'):
            #print(litag.text) 
            #print(litag.a.get('href'))
            article_name = litag.text
            article_url = litag.a.get('href')
            pages.append(article_url)
    
    articles_text = []
    
    for article in pages:
        weblink = f"https://wiki.razor.si{article}"
        raw_html = simple_get(weblink)
        soup = BeautifulSoup(raw_html, 'html.parser')
        
        mainframe = soup.find('div', {'class': 'mw-parser-output'})
        
        article_info =(weblink,
                       cleanhtml(mainframe.__str__())
        )
        articles_text.append(article_info)
        
    return articles_text

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
        