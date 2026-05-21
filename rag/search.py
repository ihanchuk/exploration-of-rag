from qdrant_client import QdrantClient, models
from qdrant_client.conversions.common_types import QueryResponse
from client_connection import get_client

client = get_client()

Collection_Name = "Rooms"

# C1.1 is the closest to the query vector,
query_vector = [0.3, 0.44, 0.51, 0.60]
search_filter = models.Filter(
    must=[models.FieldCondition(key="cat", match=models.MatchValue(value="premium"))] 
)

search_filter= models.Filter(
    must=[
        models.FieldCondition(key="cat", match=models.MatchValue(value="premium")),
        models.FieldCondition(key="price", range=models.Range(gte=100, lte=200))
    ]
)


search_results: QueryResponse = client.query_points(
    collection_name="Rooms", query=query_vector, 
    query_filter=search_filter,
    limit=3
)

if search_results.points:
    for point in search_results.points:
        print(f"Name: {point.payload['name']}")
        print(f"Price: {point.payload['price']}")
        print(f"Category: {point.payload['cat']}")
        print("----------------------------------")
