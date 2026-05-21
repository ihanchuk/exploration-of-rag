from client_connection import get_client


client = get_client()
Collection_Name = "Rooms"

collection_info = client.get_collection(collection_name=Collection_Name)

print(collection_info.points_count)
