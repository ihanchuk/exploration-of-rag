from qdrant_client import QdrantClient, models


client = QdrantClient(url="http://localhost:6333")
Collection_Name = "Rooms"

collection_info = client.get_collection(collection_name=Collection_Name)

print(collection_info.points_count)
