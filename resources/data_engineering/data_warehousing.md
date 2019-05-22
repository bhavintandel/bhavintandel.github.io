# Data Warehousing

## Fundamentals

* Dimension: structure that categorize fact and measures, commonly used are people, products, place and time. It provides structured labelling.
* Fact table: consists of measurements, metrics or fact about business process. It is located at center of STAR schema.
* Normalization: the process of organizing the columns and tables to reduce data redundancy.
* Data Marts: small datawarehouse with specific data covering certain subject area.

## Data Architecture

1. Star schema: We have fact table at center and each star endpoint has dimension table linked using foreign key. Dimension is denormalized.
2. Snowflake schema: Same as Star schema except, that dimension are also normalized. 
3. Constellation schema: contains multiple fact table which share multiple dimensions.

## DDL vs DML vs DCL vs TCL

[!commands](https://i.stack.imgur.com/7uUaJ.png)
[link](https://stackoverflow.com/questions/2578194/what-is-ddl-and-dml)
