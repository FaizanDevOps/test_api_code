import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    print(len(event['accountNo']))
    x=len(event['accountNo'])
    if x == 8:
        return {
        "statusCode": 200    
        }
    else:
        return {
        "statusCode": 400
                    }
