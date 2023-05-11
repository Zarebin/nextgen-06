import parser 
import Features from features
import Model from model



model = Model()
pages = read_pages_from_csv()

for page in pages: 
    parsed_page = parser(page)

    extractor = Features(parsed_page)
    X = extractor.get_feature_vectors()

    model.predict(X)
    
