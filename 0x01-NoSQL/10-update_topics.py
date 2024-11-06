#!/usr/bin/env python3
""" update a document in a collection """
import pymongo


def update_topics(mongo_collection, name, topics):
    """ update a document in a collection """
    if not mongo_collection:
        return None
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
