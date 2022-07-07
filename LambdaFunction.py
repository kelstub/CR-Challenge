import boto3

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('Visit_Count')

    input = {'Visits': 1}

    table.put_item(Item=input)