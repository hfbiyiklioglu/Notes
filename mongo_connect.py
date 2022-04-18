from pymongo import MongoClient
import pymongo
import yaml
from bson.binary import CSHARP_LEGACY
from bson.codec_options import CodecOptions
import pandas as pd


class MongoConnect(object):
    def __init__(self):
        # print("Base Mongo Start")
        mongo_config = yaml.load(open('config.yml'), yaml.SafeLoader)
        self.host = mongo_config['mongo_host']
        self.port = mongo_config['mongo_port']
        self.username = mongo_config['mongo_username']
        self.password = mongo_config['mongo_password']
        self.db = mongo_config['mongo_db']
        # self.collection = 'AnalyticLog1'
        self.client = MongoClient(f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}")
        # self.database = self.client[self.db]
        self.database = self.client.get_database(self.db, CodecOptions(uuid_representation=CSHARP_LEGACY))
