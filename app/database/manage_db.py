from os import getenv

from boto3 import resource
from boto3.dynamodb.conditions import Key
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
REGION_NAME = getenv("REGION_NAME")
AWS_DYNAMO_ENDPOINT = getenv("AWS_DYNAMO_ENDPOINT")


class manageDB:
    def __init__(self, name_table: str):
        dynamodb = resource(
            "dynamodb",
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=REGION_NAME,
            endpoint_url=AWS_DYNAMO_ENDPOINT,
        )
        self.table = dynamodb.Table(name_table)

    def create(self, tuple_db: dict):
        self.table.put_item(Item=tuple_db)
        return tuple_db

    def get(self, id: str):
        response = self.table.query(KeyConditionExpression=Key("id").eq(id))
        return response["Items"][0]
