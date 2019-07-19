import os
import json
import yaml
from py2neo import Graph


# Load credentials.
credentials = yaml.load(open('credentials.yml'))
username = credentials['database']['username']
password = credentials['database']['password']
url = credentials['database']['url']

# Connect to graph.
graph = Graph(url, auth=(username, password))

# Create graph.

# Build query.
query = """
WITH {json} as data
UNWIND data.data as item
MERGE (item:Outfit {id:item.itemId}) ON CREATE
  SET item.name = item.item.name, 
  item.description = item.item.description, 
  item.cost = item.item.cost,
  item.upcoming = item.item.upcoming,
  item.image = item.item.images.icon,
  item.lastUpdate = item.lastUpdate,
  item.costmeticId = item.item.costmeticId,
  item.ratingAvgStars = item.item.ratings.avgStars,
  item.ratingTotalPoints = item.item.ratings.totalPoints,
  item.ratingNumberVotes = item.item.ratings.numberVotes

MERGE (rarity:Rarity {name:item.item.rarity}) MERGE (item)-[:has_rarity]->(rarity)
MERGE (method:Method {name:item.item.obtained_type}) MERGE (item)-[:obtained_by]->(method)
MERGE (type:Type {name:item.item.type}) MERGE (item)-[:is_type]->(type)
"""

# Ingest data into graph.
with open("data/fortnite_items.json", "r") as read_file:
    data = json.load(read_file)
    graph.run(query, json=data)
