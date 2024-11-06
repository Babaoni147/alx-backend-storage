#!/usr/bin/env python3
""" insert a document in a collection """
import pymongo


def insert_school(mongo_collection, **kwargs):
    """ insert a document in a collection """
    if not mongo_collection:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
