#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
Displays:
    - Total number of log entries
    - Counts of each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Count of requests with path /status
"""

from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    Prints statistics about Nginx logs stored in MongoDB.
    Args:
        mongo_collection: MongoDB collection object
    """
    # Count total documents in the collection
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count for each HTTP method
    print("Methods:")
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count requests with path `/status`
    status_count = mongo_collection.count_documents({"method": "GET",
                                                     "path": "/status"})
    print(f"{status_count} status check")


if __name__ == "__main__":
    # Connect to MongoDB and access the collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
