## Kafka Questions

1) Kafka Memory
-> if msg_size = 100 bytes with 10k msgs/s then
throughput = 100 x 10 x 1000/(1024 x 1024) = ~ 1MB/s
with 2 broker and 3 replica, (1/2)x3 = 1.5 MB/s per broker
for Buffer of 30 sec, 45 MB per broker
 https://stackoverflow.com/questions/31301593/kafka-memory-requirement
2) Kafka and CPU requirement
3) Memory assignment to broker
4) How do add new topic with limited memory, Should we add new machines ?
5) Kafka Caching
6) Number of bytes per topic 
7) kafka performance measurement
8) Kafka partition vs Spark Partition ?
-> Each Kafka partition is mapped to individual Spark partition
9) Kafka Mirror ?
-> Its a feature to replicate kafka cluster for ex. disaster recovery. https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=27846330
10) How Spark streaming make use of kafka, for ex. 4 partition of kafka, how many spark executor of 4 cores 


Links:
1. http://kafka.apache.org/documentation/#hwandos
2. https://www.cloudera.com/documentation/kafka/latest/topics/kafka_performance.html
3. https://www.confluent.io/wp-content/uploads/confluent-kafka-definitive-guide-complete.pdf
