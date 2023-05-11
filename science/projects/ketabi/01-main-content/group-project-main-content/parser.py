import os 
import pandas as pd 
import base64
from selectolax.parser import HTMLParser
from lxml import html, etree 

# PATH_BASE refers to the unzipped directory
PATH_BASE = './project-dp-trend-description/'    

url_paths = os.listdir(PATH_BASE)
htmls_encoded = []

for file in url_paths: 
    html64file = pd.read_csv(PATH_BASE + file, nrows=10)
    htmls_encoded += html64file['html'].to_list()

sample_unicode_html = base64.b64decode(htmls_encoded[0])


pages = []
body_texts = []

for encoded_html in htmls_encoded:
    unicode_html = base64.b64decode(encoded_html)
    parsed_html = HTMLParser(unicode_html)
    body_text = parsed_html.body.text()

    if body_text.startswith('402 '):
        pass
    elif body_text.startswith('403 '):
        pass
    elif body_text.startswith('404 '):
        pass 
    else: 
        pages.append(parsed_html)


