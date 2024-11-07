!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
Displays:
    - Total number of log entries
    - Counts of each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Count of requests with path /status
"""


def log_stats(mongo_collection, option=None):
    """
    Prints statistics about Nginx logs stored in MongoDB.
    Args:
        mongo_collection: MongoDB collection object
    """
    
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)