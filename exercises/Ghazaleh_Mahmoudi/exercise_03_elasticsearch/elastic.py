from elasticsearch import Elasticsearch


es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "nextgen@123"),
    verify_certs=False
)

index_name = 'id_index'
doc_type = 'task_document'

data = [
    {'zahra' : 123},
    {'fatemeh' : 456},
    {'hadiseh' : 789},
    ]
for d in data:
    res = es.index(index=index_name, document=d)
    print(res['result'])