#!/usr/local/bin/python
# This file is a script it does not have to be imported

from os import getenv

from boto3 import resource
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = getenv("REGION_NAME")
AWS_DYNAMO_ENDPOINT = getenv("AWS_DYNAMO_ENDPOINT")

dynamodb = resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME,
    endpoint_url=AWS_DYNAMO_ENDPOINT,
)


tables = [
    {
        "TableName": "predictions",
        "KeySchema": [
            {"AttributeName": "id", "KeyType": "HASH"},
            {"AttributeName": "created_at", "KeyType": "RANGE"},
        ],
        "AttributeDefinitions": [
            {"AttributeName": "id", "AttributeType": "S"},
            {"AttributeName": "created_at", "AttributeType": "S"},
        ],
    },
]


def create_tables():
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST",
            )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    create_tables()
