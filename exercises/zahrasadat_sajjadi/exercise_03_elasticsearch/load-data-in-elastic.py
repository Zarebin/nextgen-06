from elasticsearch import Elasticsearch
import pandas as pd
from csv import DictReader


es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "nextgen@123"),
    verify_certs=False
)

index_name = 'csv_index'
doc_type = 'task_document'


# open file in read mode
with open("iris.csv", 'r') as f:
	dict_reader = DictReader(f)
	data = list(dict_reader)


for d in data:
    res = es.index(index=index_name, document=d)
    print(res['result'])
