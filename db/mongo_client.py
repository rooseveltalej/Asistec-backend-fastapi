from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

class MongoClient:
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.db = self.client[settings.DATABASE_NAME]

    def get_database(self):
        return self.db

mongo_client = MongoClient()
