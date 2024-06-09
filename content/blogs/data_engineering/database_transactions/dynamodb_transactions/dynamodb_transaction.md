Title: Dynamodb transaction
Date: 2024-05-08 22:31
Modified: 2024-05-08 22:31
Category: blogs
Tags: data-engineering
slug: de-aws-dynamodb-transaction


* Out of the box provides: Consistency and Durability from ACID.
* Atomicity strategy is multi-phase commit protocol.
* To avoid losing data for coordinator failure, coordinator state is maintained in dynamodb.
* To avoid need for failure detection, many active coordinators working on same transaction.

### Atomic writes

#### TX Records

The state of in-flight transaction stored in Dynamodb.
It has following attributes:

* Primary Key: UUID
* state: It is pending and eventually updated to committed or rolled-back
* list of Dynamodb items in transaction: Each item has id unique within transaction.
* set of update command: Each is an instruction for changing DynamoDB item.
* timestamp: approx when was transaction last worked on.
* version number: for detetcting concurrent changes to TX record.

#### Locks

Every dynamoDB item participates in protocol needs to have lock attribute and its null string, but when item is pariticipating in transaction then lock is set to primary key of the transaction record. It contains,
* applied flag
* transient flag
* timestamp 

#### Item Images

After each item is locked and before its changed during transaction, 
a complete previous copy of the item is kept in the transaction table. So that we can roll back during error.
Each item imgae has,
* all attributes of item befor its modified.
* primary key of the transaction.
* unique id within transaction.


## Reference
https://github.com/awslabs/dynamodb-transactions/blob/master/DESIGN.md


## Transactions using Dynamodb boto3

### Write items

**transact_write_items** is synchronous write operation that group upto 25 action requests, with upto 4 MB of data.
Following are the api available:
  * Put
  * Update
  * Delete
  * ConditionCheck 


## Blog content

quote ""

We live a society where partial information can be more dangerous than full information. This pyscology plays 
major role in an software application life. If you work in application development field, odds are very high that you have worked with some external 
storage system along with your applications. It can be for saving the information crunch by the application or
storing the current state of your application.

The real world is not perfect neither it can be made, But we can learn to handle the situation.
Lets not get too philosophical and get to the point. 
Consider a scenario, you own an *Online shopping market*.
You have maintained two tables, order table and dispatch table. 
Order table contains information regarding order details. Now for instance whenever an order is processed
you add flag to your item in order table notifying that the order is completed and
you add new item into dispatch table which indicate that new item has to be dispatched.

Scenario 1: The perfect world for everyone

Order table flagged and new item added to Dispatch table.

Scenario 2: Awesome world for user

Order table flagged and new item added twice in the Dispatch.

Scenario 3: Worst world for you

Order table flagged and new item not added to dispatch.

Now as we have seen these 3 scenario, we know that both of these tasks(Flagging Order table and Adding item to Dispatch table) should be either successful or 
both should roll back to previous state.

To tackle these, you can develop your own custom highly intelligent software which considers all the scenario, 
and can handle any environment. Or you can use the storage system which have the capabilities to handle such issues.

For our this scenario, it would make sense if we use the transactions capabilities of the system so that it will either update
both items or it wont update any.

