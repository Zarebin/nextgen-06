import re
from Modules import unicode_convertor, html_parser
from hazm import word_tokenize, sent_tokenize, stopwords_list, Normalizer


def tokenize_contents(html_parser_tags):
    """This function has to prepare sentences for our corpus and even prepare unique words used in our content"""
    clear_contents = ""

    for tag in html_parser_tags:
        clear_contents += tag.text

    normalizer = Normalizer()
    clear_contents = normalizer.normalize(clear_contents)
    clear_contents_wo_punct = re.sub(r'[^\w\s]','',clear_contents)
    sentences = sent_tokenize(clear_contents)
    stops = set(stopwords_list())
    words = [[word for word in word_tokenize(sentence) if word not in stops] for sentence in sent_tokenize(clear_contents_wo_punct)]

    return (sentences, words)


