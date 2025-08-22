from dataclasses import dataclass
import os
import pymongo

@dataclass

class Enviornmentalvariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")
    
    
env_var = Enviornmentalvariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)