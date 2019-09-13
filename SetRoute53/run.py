from lambda_function import lambda_handler, gen_hash
import config

if __name__ == "__main__":
    ip = '192.168.1.69'
    generated_hash = gen_hash(ip, config.secret)
    event = {
        "body-json" : {
            "ip": ip,
            "hash": generated_hash
        },
        "ip": ip
    }
    
    lambda_handler(event, {})