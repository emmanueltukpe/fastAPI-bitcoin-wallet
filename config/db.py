from pymongo import MongoClient
from pymongo.collection import Collection

# # Package # #
from settings import mongo_settings as settings

__all__ = ("client", "collection")

client = MongoClient(settings.uri)
user_collection: Collection = client[settings.database][settings.user_collection]
wallet_collection: Collection = client[settings.database][settings.wallet_collection]
transaction_collection: Collection = client[settings.database][settings.transaction_collection]
