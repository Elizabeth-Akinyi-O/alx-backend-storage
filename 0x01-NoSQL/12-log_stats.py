#!/usr/bin/env python3

""" Provides some stats about Nginx logs stored in MongoDB. """

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')

    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in http_methods:
        print("\tmethod {}: {}".format(method,
                                       nginx_collection.count_documents
                                       ({"method": method})))

    print("{} status check".format(nginx_collection.count_documents({
                                   "method": "GET", "path": "/status"})))
