from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from .configuration import URI, create_collection


def connection():

    try:
        client = MongoClient(URI)
    except ConfigurationError:
        print("Connection failed")
    else:
        database = client["bunyols-library"]
        if "catalog" not in database.list_collection_names():
            create_collection(database)

        collection = database["catalog"]
        return collection
