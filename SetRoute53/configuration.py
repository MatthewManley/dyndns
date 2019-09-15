import json
import os

class Configuration:
    zone_id: str = None
    record_name: str = None
    record_type: str = None
    secret: str = None
    require_same_ip: bool = None

    def __init__(self, config_file: str):
        with open(config_file, 'r') as file:
            self.__dict__ = json.load(file)
