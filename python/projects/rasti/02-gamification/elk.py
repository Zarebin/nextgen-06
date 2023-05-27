from elasticsearch import Elasticsearch
import json
import os
import warnings
warnings.filterwarnings("ignore")

es = Elasticsearch("https://localhost:9200", basic_auth=('elastic', 'Q1ZCm-txxbqPLWPlIWSl'), verify_certs=False)

with open(os.path.abspath('').replace('\\', '/')+ '/data/gamification_events.json') as f:
    events_json = json.load(f)

index_name = 'gamificiation_events_all'
for i, e in enumerate(events_json):
    res = es.index(index=index_name, document=e)
    if i % 100000 == 0:
        print(i, '-', res['result'])