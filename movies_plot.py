from elasticsearch import Elasticsearch
import pandas as pd
es = Elasticsearch("http://localhost:9200")
es.info().body

# df = (
#     pd.read_csv("wiki_movie_plots_deduped.csv")
#     .dropna()
#     .sample(5000, random_state=42)
#     .reset_index()
# )
#
# mappings = {
#         "properties": {
#             "title": {"type": "text", "analyzer": "english"},
#             "ethnicity": {"type": "text", "analyzer": "standard"},
#             "director": {"type": "text", "analyzer": "standard"},
#             "cast": {"type": "text", "analyzer": "standard"},
#             "genre": {"type": "text", "analyzer": "standard"},
#             "plot": {"type": "text", "analyzer": "english"},
#             "year": {"type": "integer"},
#             "wiki_page": {"type": "keyword"}
#     }
# }
#
# es.indices.create(index="movies2", mappings=mappings)
#
# for i, row in df.iterrows():
#     doc = {
#         "title": row["Title"],
#         "ethnicity": row["Origin/Ethnicity"],
#         "director": row["Director"],
#         "cast": row["Cast"],
#         "genre": row["Genre"],
#         "plot": row["Plot"],
#         "year": row["Release Year"],
#         "wiki_page": row["Wiki Page"]
#     }
#     es.index(index="movies2", id=i, body=doc)

response = es.search(
    index="movies2",
    body={
        "query": {
            "bool": {
                "must": {
                    "match": {
                        "cast": "jack nicholson"
                    }
                },
                "must_not": {
                    "match": {
                        "director": "roman polanski"
                    }
                }
            }
        }
    }
)

print(response)
for hit in response['hits']['hits']:
    print(f'Title: {hit["_source"]["title"]}, Director: {hit["_source"]["director"]}, Cast: {hit["_source"]["cast"]}')


