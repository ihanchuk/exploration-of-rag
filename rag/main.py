from qdrant_client import QdrantClient, models


client = QdrantClient(url="http://localhost:6333")

points = [
    models.PointStruct(
        id=1, vector=[0.1, 0.2, 0.3, 0.4], payload={"name": "Room A", "price": 50}
    ),
    models.PointStruct(
        id=2, vector=[0.2, 0.3, 0.4, 0.5], payload={"name": "Room B", "price": 100}
    ),
    models.PointStruct(
        id=3, vector=[0.3, 0.4, 0.5, 0.62], payload={"name": "Room C", "price": 200}
    ),
    models.PointStruct(
        id=4, vector=[0.3, 0.44, 0.51, 0.62], payload={"name": "Room C1", "price": 220}
    ),
]


def main():
    Collection_Name = "Rooms"
    Vector_Config = models.VectorParams(size=4, distance=models.Distance.COSINE)

    if client.collection_exists(collection_name=Collection_Name):
        client.delete_collection(collection_name=Collection_Name)

    client.create_collection(collection_name=Collection_Name, vectors_config=Vector_Config)

    client.upsert(
        collection_name=Collection_Name,
        points=points,
    )

    print("Hello from rag!")
    print(client.get_collections())


if __name__ == "__main__":
    main()
