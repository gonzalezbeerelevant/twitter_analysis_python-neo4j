from neo4j import Graph Database

### Auth ###
uri = "bolt://3.83.167.43:7687"
user = "neo4j"
password = "turpitude-meanings-longitude"

driver = GraphDatabase.driver(uri, auth=(user, password))


class HelloWorldExample:

    # def __init__(self, uri, user, password):
    #     self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    #greeter = HelloWorldExample("bolt://3.83.167.43:7687", "neo4j", "turpitude-meanings-longitude")
    greeter.print_greeting("hello, world")
    greeter.close()