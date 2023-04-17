import re
from builtins import str

import pandas as pd
import base64
from hazm import stopwords_list, word_tokenize, sent_tokenize
from bs4 import BeautifulSoup


def get_clear(csv_address):


    ana_all = pd.read_csv("C:\\Users\\Behnam\\Downloads\\project-dp-trend-description\\ana_press_all.csv")
    binary_file_data = ana_all['html']

    base64_message = binary_file_data[0]
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    Html = message_bytes.decode('utf-8')

    # print(Html)

    # VALID_TAGS = ['p']

    soup = BeautifulSoup(Html, features="html.parser")

    contents = soup.findAll('p')

    sentences = []

    clear_contents = ""

    corpus = []

    for item in contents:
        temp = str(item.text).replace('\u200c', '')
        temp = temp.split(".")
        temp = [item for item in temp if item]
        # temp = str(temp).replace()
        # temp = re.sub(r'[^\w]', ' ', temp)
        # if temp != '' and temp!:
        corpus.append(temp)

    # corpus.append(re.sub(r'[^\w]', ' ', str(item.text).replace('\u200c', '')).split("."))

    for item in contents:
        sentences.append(re.sub(r'[^\w]', ' ', str(sent_tokenize(str(item.text).replace('\u200c', '')))))
        # print(item)
    # print(sentences)

    for i in range(len(sentences)):
        clear_contents += sentences[i]
        # corpus.append(sentences[i])

    sentence = clear_contents
    words = word_tokenize(sentence)
    words = [word for word in words if not word in stopwords_list()]
    return (words, corpus)
