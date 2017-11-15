import os, sys

script_dir = os.path.dirname( os.path.realpath(__file__) )
sys.path.insert(0, script_dir + os.sep + "lib")

import logging, json
log = logging.getLogger()
log.setLevel(logging.INFO)


def handler(event, context):
  return response(
      {"message": "Terve Topconf!"}, event)


def response(body, event, code=200):
  if 'resource' in event and 'httpMethod' in event:
    return {
        'statusCode': code,
        'headers': {},
        'body': json.dumps(body, indent=4, separators=(',', ':')) 
      }
  return body