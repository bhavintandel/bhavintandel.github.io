import boto3
import pytest
from moto import mock_dynamodb
#from dynamodbtransact import dynamodb_transactions


class TestDynamodbTransactions(object):

    @pytest.yield_fixture(scope="module")
    def set_up(self):
        self.mock_dynamodb = mock_dynamodb().start()
        dynamodb_client = boto3.client("dynamodb")
        dynamodb_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'col_id',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'first_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'last_name',
                    'AttributeType': 'S'
                }
        ],
        TableName='TestTable',
        KeySchema=[
            {
                'AttributeName': 'col_id',
                'KeyType': 'HASH'
            }
        ]
        )
        yield "Connected"
        print("Teardown...")
        self.mock_dynamodb.stop()

    def test_dynamodb_transact(self, set_up):
        print("Pass")
        dynamodb_client = boto3.client("dynamodb")
        dynamodb_client.list_tables()
        #dynamodb_transactions.update_items_with_transact()
