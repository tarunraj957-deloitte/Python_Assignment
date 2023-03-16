import os

from boto3 import resource
from boto3.dynamodb.conditions import Key, Attr
from django.conf import settings
import pandas as pd
import json
from decimal import Decimal
import schedule
import time

AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
REGION_NAME = settings.REGION_NAME
ENDPOINT_URL = settings.ENDPOINT_URL

resource = resource(
    'dynamodb',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)
movies_json = json.loads(
    pd.read_csv('/home/tlohar/PycharmProjects/Movie/Movie/static/movies.csv').to_json(orient='records'),
    parse_float=Decimal)
print(movies_json[1])


def create_table_movie():
    print(AWS_SECRET_ACCESS_KEY, AWS_ACCESS_KEY_ID, REGION_NAME, ENDPOINT_URL)
    table = resource.create_table(
        TableName='Movie',
        KeySchema=[
            {
                'AttributeName': 'imdb_title_id',
                'KeyType': 'HASH'
            }

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'imdb_title_id',
                'AttributeType': 'S'
            },
        ],

        ProvisionedThroughput={
            'ReadCapacityUnits': 100,
            'WriteCapacityUnits': 100
        }

    )

    return table


dynamoTable = resource.Table('Movie')


def read_csv_file():
    print("entered")
    with dynamoTable.batch_writer() as batch:
        for item in movies_json:
            batch.put_item(Item=item)

    return dynamoTable


def read_movie(director, year1, year2):
    response = dynamoTable.scan(
        FilterExpression=Attr('director').eq(director) & (Attr('year').gte(year1) & Attr('year').lte(year2)),
    )

    data = response['Items']
    titles = []
    for i in data:
        titles.append(i['title'])  # appending titles to list

    return titles


#below function return englishtitles
def review_movie(review):
    response = dynamoTable.scan(
        FilterExpression=Attr('reviews_from_users').gt(review)
    )
    data = response['Items']
    english_titles = []
    for i in data:
        if i['language'] == 'English':
            english_titles.append(i['title'])  # appending titles to list
    english_titles.sort(reverse=True)

    return english_titles

