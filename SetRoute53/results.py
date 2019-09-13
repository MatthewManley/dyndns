
# Used when the client reports an IP address different from its own
invalid_ip_address = {
    'statusCode': 41,
    'description': 'Reported IP address does not match the clients IP address'
}

# Used when the client doesn't know the right secret
invalid_secret = {
    'statusCode': 42,
    'description': 'Client provided an invalid secret'
}

# Succesfully authenticated but did not need updating
success_no_update = {
    'statusCode': 20,
    'description': 'Record did not need updating'
}

success_changed = {
    'statusCode': 21,
    'description': 'Record updated'
}