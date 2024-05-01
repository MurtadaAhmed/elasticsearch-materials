from elasticsearch import Elasticsearch
import io
es = Elasticsearch("http://localhost:9200")

print(es.ping())

with io.open("test_index_names.txt", "r", encoding="utf-8") as f1:
    data = f1.read()
    f1.close()

data = data.split("\n")

for index in data:
    response = es.indices.create(index=index)
    print(response)


# creating an index
# es.indices.create(index="tutorial")

# get all indices:
# indices=es.indices.get_alias(index="*")
#
# for index in indices:
#     print(index)

# create index with sequence:
# index_basename = "test_base_name"
#
# for i in range(1, 11):
#     response = es.indices.create(index=index_basename+"_"+str(i))
#     print(response)

