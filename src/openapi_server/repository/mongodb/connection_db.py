import os
from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

class ConnectionDB:
    def __init__(self):
        try:
            mongo_url = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
            mongo_user = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
            mongo_pass = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'example')

            self.client = MongoClient(f"mongodb://{mongo_user}:{mongo_pass}@mongo:27017/?authSource=admin")
            self.db = self.client[os.getenv('MONGO_INITDB_DATABASE', 'peak-db')]
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")

    def get_collection(self, collection_name: str):
        """
        Return the collection of the database
        """
        return self.db[collection_name]
