review...

# <strong>Analisando tweets com Neo4j</strong>

O objetivo deste projeto é demonstrar os passos necessários para se realizar uma análise de tweets baseada em grafos.
Nele, irei utilizar o banco de dados baseado em grafos Neo4j e abordarei conceitos principais como modelagem, ingestão dos dados e análise utilizando a linguagem Cypher.


### <strong>Etapa 1 - Modelagem dos dados</strong>


**Nós**
- User: Representa um usuário do Twitter (Identificador)
- Tweet: Representa um tweet (Texto)

**Relacionamentos**
- TWEETED: Relacionamento entre User e Tweet. Indica que este usuário é autor do tweet
- RETWEETED: Relacionamento entre User e Tweet. Indica que este usuário retuitou este tweet








hrefs:
- https://neo4j.com/blog/twitter-hashtag-impact-neo4j-python-javascript/