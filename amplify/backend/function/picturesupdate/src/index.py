import json
import datetime

def handler(event, context):

  current_time = datetime.datetime.now().time()

  body = {
      'message': 'Hello, the current time is ' + str(current_time)
  }

  response = {
      'statusCode': 200,
      'body': json.dumps(body),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://dev.d3pg0y1aa3erd4.amplifyapp.com',
        'Access-Control-Allow-Methods': 'OPTIONS,POST',
        'Access-Control-Allow-Headers': 'Content-Type'
      },
  }
  return response