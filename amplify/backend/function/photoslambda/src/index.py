import boto3
from botocore.exceptions import ClientError
import uuid
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('dynamodb')

def handler(event, context):
  logger.info("Request: %s", event)
  response_code = 200

  http_method = event.get('httpMethod')
  query_string = event.get('queryStringParameters')
  headers = event.get('headers')
  body = event.get('body')
  path = event.get('pathParameters')

  if http_method == 'GET':
    greeting = f"Got your GET, {path}."
    data = client.scan(
      TableName='photopost'
    )
  elif http_method == 'POST':
    uuid_inserted = uuid.uuid4().hex
    data = client.put_item(
      TableName='photopost',
      Item={
          'id': uuid_inserted,
          'name': body['name'],
          'description': body['description'],
          'image': body['image']
      }
    )
  elif http_method == 'PUT':
      greeting = f"I'll just PUT this here for you, {path}."
  else:
      greeting = f"Sorry, {path}, {http_method} isn't allowed."
      response_code = 405

  response = {
      'statusCode': response_code,
      'body': json.dumps({'input': data}),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
  }

  logger.info("Response: %s", response)
  return response

    
