"""
Code snippet for transactions in dynamodb
"""


def update_items_with_transact(dynamodb_client, transact_items):
    """
    Updates the dynamodb items with transactions
    :param dynamodb_client:
    :param transact_items: list of transactions item
    """
    
    response = dynamodb_client.transact_write_items(
        TransactItems=transact_items,
    )