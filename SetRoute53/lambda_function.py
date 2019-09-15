import json
import boto3
import hashlib
import results
from configuration import Configuration
from boto3_type_annotations.route53 import Client as Route53Client

def lambda_handler(event, context):
    route53: Route53Client = boto3.client('route53')
    config = Configuration("config.json")
    ip = event['ip']
    client_body = event['body-json']

    # Checks that the ip address the client reports is the ip address of the client
    if config.require_same_ip and client_body['ip'] != ip:
        return results.invalid_ip_address
    
    # Ensures the client knows the secret
    calculated_hash = gen_hash(ip, config.secret)
    if client_body['hash'] != calculated_hash:
        return results.invalid_secret

    # Fetch the current Route53 record value
    record = get_record(route53, config)

    # The Route53 record is up to date, do nothing and return success
    if record == ip:
        return results.success_no_update

    #TODO: Update record if different
    
    return results.success_changed
    
def get_record(route53Client: Route53Client, config: Configuration):
    response = route53Client.list_resource_record_sets(
        HostedZoneId=config.zone_id,
        StartRecordName=config.record_name,
        StartRecordType=config.record_type,
        MaxItems='1'
        )
    
    # Search for a record in the record set where Name == record_name and Type == 'A'
    check_valid_record = lambda x: x['Name'] == config.record_name and x['Type'] == config.record_type
    record_set = list(filter(check_valid_record, response['ResourceRecordSets']))
    
    assert len(record_set) == 1
    records = record_set[0]['ResourceRecords']
    assert len(records) == 1
    return records[0]['Value']

def gen_hash(ip, secret):
    combined = ip+secret
    return hashlib.sha512(combined.encode("utf-8")).hexdigest()
