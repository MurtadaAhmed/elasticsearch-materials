from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{"host": "localhost", "port": 9200, "scheme": "http"}], verify_certs=False)
books = [
    {"title": "Book 1", "author": "Author 1", "year": "2020"},
    {"title": "Book 2", "author": "Author 2", "year": "2021"},
    {"title": "Book 3", "author": "Author 3", "year": "2022"},
    {"title": "Book 4", "author": "Author 4", "year": "2023"},
    {"title": "Book 5", "author": "Author 5", "year": "2024"},
    {"title": "Book 6", "author": "Author 6", "year": "2025"},
    {"title": "Book 7", "author": "Author 7", "year": "2026"},
    {"title": "Book 8", "author": "Author 8", "year": "2027"},
    {"title": "Book 9", "author": "Author 9", "year": "2028"},
    {"title": "Book 10", "author": "Author 10", "year": "2029"},
]

for i, book in enumerate(books):
    es.index(index="library", id=i, body=book)


def search_books(query):
    result = es.search(index="library", body={"query": {"match": {"title": query}}})
    if result["hits"]["total"]["value"] > 0:
        print("Search Results:")
        for hit in result["hits"]["hits"]:
            print(f"Title: {hit['_source']['title']}, Author: {hit['_source']['author']}, Year: {hit['_source']['year']}")
    else:
        print("No results found")

# search_books("Book 1")
# search_books("Book 2")
search_books("2")