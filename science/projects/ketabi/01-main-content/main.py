from page_parser import PageParser
from features import Features
from model import *
import time

base_path = 'project-dp-trend-description/'

#Parsing
parser = PageParser()
parsed_pages = parser.parse_batch(path=base_path)


#Feature Extraction
features = np.zeros(len(parsed_pages))
labels = np.zeros(len(parsed_pages))
for i, page in enumerate(parsed_pages): 
    extractor = Features(page)
    feature, label, _ = extractor.get_feature_vectors()
    print(feature, '\n', label)
    features[i] = feature
    labels[i] = label 


#Modeling
model = ModelClass(features, labels).trainer(type = 'random forest')


preds = model.predict()
labels_test = model.y_test

import seaborn as sns 
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt 
cm = confusion_matrix(preds, labels_test)
sns.heatmap(cm, annot=True)






def predict_new_page(url, model): 
    parsed_page = parser.parse_single_url(url)
    s_time = time.time()
    features, _, nodes = Features(parsed_page).get_feature_vectors()
    preds = model.predict(features)
    f_time = time.time()
    print((f_time - s_time) * 1000, ' ms')
    return nodes[np.array(preds).argmax()]



url = 'https://www.namehnews.com/%D8%A8%D8%AE%D8%B4-%DA%AF%D9%88%DA%AF%D9%84-%D9%86%DB%8C%D9%88%D8%B2-66/678317-%D8%AC%D8%B2%D8%A6%DB%8C%D8%A7%D8%AA-%D9%86%D8%A7%D9%85%D9%87-%D9%85%D9%87%D9%85-%D9%86%D9%85%D8%A7%DB%8C%D9%86%D8%AF%DA%AF%D8%A7%D9%86-%D9%85%D8%AC%D9%84%D8%B3-%D8%A8%D9%87-%D8%B1%D9%87%D8%A8%D8%B1-%D8%A7%D9%86%D9%82%D9%84%D8%A7%D8%A8'
node = predict_new_page(url, model)
node.text()