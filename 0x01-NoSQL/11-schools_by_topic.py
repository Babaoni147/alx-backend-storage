#!/usr/bin/env python3
""" list all documents in a collection """
import pymongo


def schools_by_topic(mongo_collection, topic):
    """ list all documents in a collection """
    if not mongo_collection:
        return []
    return mongo_collection.find({"topics": topic})
