

# use elastic search API
import requests
response = requests.get("http://localhost:9200/_cat/indices?format=json")
data = response.json()
[print(row["index"]) for row in data]
# create index using elastic API
create_index = requests.put("http://localhost:9200/test_index_using_api")
print(create_index.text)
# search index using API
index_name = "library"
search_result = requests.get("http://localhost:9200/" + index_name)
print(search_result.text)



# from elasticsearch import Elasticsearch
# import io
# es = Elasticsearch("http://localhost:9200")
#
# print(es.ping())




# delete indices from file:
# with io.open("test_index_names.txt", "r", encoding="utf-8") as f1:
#     data = f1.read()
#     f1.close()
# data = data.split("\n")
# for index in data:
#     response = es.indices.delete(index=index)
#     print(response)


# delete index
# index = "movies"
# response=es.indices.get_alias(index=index)
# for index in response:
#     es.indices.delete(index=index)


# search elasticsearch index
# index = "tutorial"
# response=es.search(index=index)
# print(response)


# create index from .txt file
# with io.open("test_index_names.txt", "r", encoding="utf-8") as f1:
#     data = f1.read()
#     f1.close()
#
# data = data.split("\n")
#
# for index in data:
#     response = es.indices.create(index=index)
#     print(response)


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

