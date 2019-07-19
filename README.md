# Fortnite Fashionista

**Welcome to the [Fortnite](https://www.epicgames.com/fortnite/en-US/home) Knowledge Graph!**

We are working on some cool new features for you :D

Star this repository on GitHub and follow [@GeorgeCushen](https://twitter.com/georgecushen) to be notified of updates.

## Prerequisites

1. Download and install [Neo4j Desktop (Community Edition)](https://neo4j.com/download/).
2. Open Neo4j Desktop and create a new database
3. Start your new database
4. Install Pipenv: `pip install -U pipenv`

## Quick Start

1. Clone or download Fortnite Fashionista
2. Open Terminal and navigate to the Fortnite Fashionista folder
3. Add your Neo4j graph database credentials in `credentials.yaml`
4. `pipenv install`
5. `pipenv shell`
6. `python create_graph.py`

## Explore, Query, and Analyse

Open *Neo4j Browser* from the applications panel in Neo4j Desktop.

Use [Cypher](https://neo4j.com/developer/cypher-query-language/) to query the graph.

### Examples

To view a subset of the entire graph: `MATCH (n) RETURN n LIMIT 300`

## Contribute

Please help improve this project by submitting a PR :)
