from page_parser import * 
from features import *
from model import *

base_path = './project-dp-trend-description/'

model = Model()
parser = PageParser()

parsed_pages = parser.parse_batch(path=base_path)
extractor = Features(parsed_pages)
X = extractor.get_feature_vectors()
model.predict(X)
    
