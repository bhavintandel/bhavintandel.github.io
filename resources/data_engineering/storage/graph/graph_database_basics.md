## Graph Database 
Once we understand graphs, we
begin to see them in all sorts of places. Gartner, for example, identifies five graphs in the world of business—
  * social
  * intent
  * consumption
  * interest
  * mobile

### Labeled property graph
• It contains nodes and relationships.
• Nodes contain properties (key-value pairs).
• Nodes can be labeled with one or more labels.
• Relationships are named and directed, and always have a start and end node.
• Relationships can also contain properties.

### Graph space can be categorized in:
  1. Graph database
    * These technologies are called graph databases and are the main focus of neo4j. They are the equivalent of “normal” online transactional processing (OLTP) databases in the relational world

  2. Graph compute engine
    * They can be thought of as being in the same category as other technologies for analysis of data in bulk, such as data mining and online analytical processing (OLAP).

**Graph space can also be described as graph models employed by various technologies**
Dominant graph models are:
  1. The property graph
  2. Resource descriptor framework (RDF) triples and 
  3. Hypergraph

Neo4j used the property graph model


### Querying graph db

Queries are not case sensitive but labels are case sensitive.

#### Find 

  * Find Actor Tom Hanks
  `MATCH (tom {name: "Tom Hanks"}) RETURN tom`

  * Find 10 people, this will list names of 10 people.
  `MATCH (people:Person) RETURN people.name LIMIT 10

  * Where clause in the query
  `MATCH (nineties:Movie) WHERE nineties.released > 1990 AND nineties.released < 2000 RETURN nineties.title`


#### Query

  * Listing tom hanks movies
  `MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies`

  * Find the director of cloud atlas
  `MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name`
  Above query can also be written as,
  `MATCH ({title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name`

  * Tom hansk co-actor
  `MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name`