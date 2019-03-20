## Kafka important points
* Any events that need to stay in fixed order should go in same topic and must use the same partition key.
* For each replicated partition, only one broker is the leader. It’s the leader of a partition that producers and consumers interact with.