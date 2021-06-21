# from neo4j import GraphDatabase

# #uri = "neo4j://localhost:7687"
# uri = 'bolt+s://660f8e2a7742832bf0470ec7f2e2277a.neo4jsandbox.com:7687'
# driver = GraphDatabase.driver(uri, auth=("neo4j", "alleys-increments-subtotals"))

# def create_friend_of(tx, name, friend):
#     tx.run("MATCH (a:Person) WHERE a.name = $name "
#            "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
#            name=name, friend=friend)

# with driver.session() as session:
#     session.write_transaction(create_friend_of, "Alice", "Bob")

# with driver.session() as session:
#     session.write_transaction(create_friend_of, "Alice", "Carl")

# driver.close()

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://3.238.164.132:7687",
  auth=basic_auth("neo4j", "alleys-increments-subtotals"))

cypher_query = '''
MATCH (n)
RETURN COUNT(n) AS count
LIMIT $limit
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      limit="10").data())
  for record in results:
    print(record['count'])

driver.close()