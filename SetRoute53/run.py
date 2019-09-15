from lambda_function import lambda_handler, gen_hash
from configuration import Configuration

# This file is for running locally, so that we don't have to constantly upload to aws
if __name__ == "__main__":
    ip = '192.168.1.69'
    config = Configuration("config.json")
    generated_hash = gen_hash(ip, config.secret)
    event = {
        "body-json" : {
            "ip": ip,
            "hash": generated_hash
        },
        "ip": ip
    }
    
    lambda_handler(event, {})