import json

class config:
    zone_id: str = None
    record_name: str = None
    record_type: str = None
    secret: str = None

    def __init__(config_file: str):
        config_obj = json.loads(config_file)
        zone_id = config_obj['zone_id']
