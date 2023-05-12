import os 
import base64
from selectolax.parser import HTMLParser
from lxml import html 
import pandas as pd 

class PageParser():
    def __init__(self, ): 
        self.PATH_BASE = './project-dp-trend-description/' 
        

    def _read_batch(self, path):
        url_paths = os.listdir(self.PATH_BASE)
        htmls_encoded = []

        for file in url_paths: 
            html64file = pd.read_csv(path + file, nrows=10)
            htmls_encoded += html64file['html'].to_list()
        return htmls_encoded



    def parse_batch(self, path, option='lxlm'):
        parsed_pages = []
        htmls_encoded = self.read_batch(path) if path else self.PATH_BASE

        for encoded_html in htmls_encoded:
            unicode_html = base64.b64decode(encoded_html)

            if option == 'lxlm': 
                parsed_html = html.fromstring(unicode_html)
            elif option == 'selectolax': 
                parsed_html = HTMLParser(unicode_html)

            body_text = parsed_html.body.text()
            if body_text.startswith('402 '):
                pass
            elif body_text.startswith('403 '):
                pass
            elif body_text.startswith('404 '):
                pass 
            else: 
                parsed_pages.append(parsed_html)

        print(len(parsed_pages), 'of', len(htmls_encoded), 
            'were read successfuly!')
        return parsed_pages



    def parse_single_url(self, url, option='lxml'):
        if option == 'lxlml': 
            parsed_html = html.fromstring(url)
        elif option == 'selectolax': 
            parsed_html = HTMLParser(url)
        body_text = parsed_html.body.text()

        if body_text.startswith('402 '):
            print('failed to read the page due to Error 402')
        elif body_text.startswith('403 '):
            print('failed to read the page due to Error 403')
        elif body_text.startswith('404 '):
            print('failed to read the page due to Error 404') 
        else: 
            return parsed_html

