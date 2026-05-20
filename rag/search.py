from qdrant_client import QdrantClient

client = QdrantClient(url="http://localhost:6333")

Collection_Name = "Rooms"

query_vector = [0.3, 0.39, 0.49, 0.59]

search_results = client.query_points(
    collection_name="Rooms",
    query=[0.3, 0.39, 0.49, 0.59],
    limit=10
)

print(search_results.points[0].payload["name"])

