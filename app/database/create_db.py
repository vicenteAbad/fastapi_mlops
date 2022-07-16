#!/usr/local/bin/python
# This file is a script it does not have to be imported

from os import getenv

from boto3 import resource

dynamodb = resource(
    "dynamodb",
    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=getenv("REGION_NAME"),
    endpoint_url="http://localhost:8000",
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
