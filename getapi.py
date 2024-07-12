import json

def lambda_handler(event, context):
    
    print(f'event: {event}');
    
    # this users object can be fetched from database  etc.
    users =  [
                {"id": 1, "name": "faizan shaikh"}, 
                {"id": 2, "name": "it vedant "}
             ]
        
    return {
        'statusCode': 200,
        'body': json.dumps(users)
    }
