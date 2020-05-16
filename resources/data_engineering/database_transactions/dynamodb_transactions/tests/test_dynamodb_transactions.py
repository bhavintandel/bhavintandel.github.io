import pytest
from moto import mock_dynamodb2


class TestDynamodbTransactions(object):

    @pytest.yield_fixture(scope="module")
    def set_up(self):
        self.mock_dynamodb2 = mock_dynamodb2().start()
        yield "Connected"
        print("Teardown...")
        self.mock_dynamodb2.stop()

    def test_dynamodb_transact(self, set_up):
        print("Pass")
