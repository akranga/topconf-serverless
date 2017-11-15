import os, sys

script_dir = os.path.dirname( os.path.realpath(__file__) )
sys.path.insert(0, script_dir + os.sep + "lib")

import logging, json, boto3, random
from boto3.dynamodb.conditions import Attr

log = logging.getLogger()
log.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMO_TABLE'])

def handler(event, context):
  num  = random.randint(1,65)
  resp = table.scan(
           FilterExpression=Attr('Num').eq( str(num) )
          )['Items'][0]

  return response(
      resp, event)


def response(body, event, code=200):
  if 'resource' in event and 'httpMethod' in event:
    return {
        'statusCode': code,
        'headers': {},
        'body': json.dumps(body, indent=4, separators=(',', ':')) 
      }
  return body