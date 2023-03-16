#
# import boto3
# import pandas as pd
# import json  # Access Credentials
# from decimal import Decimal
#
# a_data = pd.read_csv('movies.csv')
# a_key = 'key99'
# a_S_key = 'key99'
# region = 'us-east-2'
# ENDPOINT_URL = 'http://localhost:8000'
#
# movies_json = json.loads(pd.read_csv('movies.csv').to_json(orient='records'), parse_float=Decimal)
# dynamodb = boto3.resource('dynamodb', aws_access_key_id=a_key, aws_secret_access_key=a_S_key, region_name=region,
#                           endpoint_url=ENDPOINT_URL)
#
# print(dynamodb)
#
# table = dynamodb.create_table(
#     TableName='Movie007',
#     KeySchema=[
#         {
#             'AttributeName': 'imdb_title_id',
#             'KeyType': 'HASH'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'imdb_title_id',
#             'AttributeType': 'S'
#         },
#     ],
#
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 100,
#         'WriteCapacityUnits': 100
#     }
#
# )
# dynamoTable = dynamodb.Table('Movie007')
# with dynamoTable.batch_writer() as batch:
#     for item in movies_json:
#         batch.put_item(Item=item)
