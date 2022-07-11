import boto3
import json


def lambda_handler(event, context):
   return {
    'statusCode': 200,
    'body': json.dumps('Hello, World!')
}


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Visit_Count')
input = {'Visits': 23}
table.put_item(Item=input)