#!/usr/bin/env python3

"""Provides some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def nginx_stats():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    # Select the database and collection
    db = client.logs
    nginx_collection = db.nginx
    # Get the total number of logs
    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")
    # List of HTTP methods
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    # Print stats for each HTTP method
    print("Methods:")
    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    # Count for GET requests to /status
    status_check_count = nginx_collection.count_documents(
                                     {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == '__main__':
    nginx_stats()
