from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from backend.config import settings

class VectorDBService:
    def __init__(self):
        try:
            self.client = QdrantClient(host=settings.QDRANT_HOST, port=settings.QDRANT_PORT)
            self.collection_name = settings.QDRANT_COLLECTION
            self._ensure_collection()
            self.is_connected = True
        except Exception as e:
            print(f"Warning: Could not connect to Qdrant: {e}")
            self.is_connected = False

    def _ensure_collection(self):
        collections = self.client.get_collections().collections
        if not any(c.name == self.collection_name for c in collections):
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=768, distance=Distance.COSINE),
            )

    def insert(self, text: str, vector: list, payload: dict = None):
        if not self.is_connected: return False
        # Simplified insert
        import uuid
        from qdrant_client.http.models import PointStruct
        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"text": text, **(payload or {})}
        )
        self.client.upsert(
            collection_name=self.collection_name,
            wait=True,
            points=[point]
        )
        return True

    def search(self, vector: list, limit: int = 5):
        if not self.is_connected: return []
        return self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=limit
        )

vector_db = VectorDBService()
