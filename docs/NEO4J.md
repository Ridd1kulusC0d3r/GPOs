# Neo4j export

Generate graph-import CSV:

```bash
python scripts/export_neo4j.py --output exports/neo4j
```

Outputs:

- `nodes.csv`
- `relationships.csv`

The graph includes GPO controls, ATT&CK techniques, D3FEND techniques, Windows Event IDs, profiles, threat packs and actor overlays.

Example Cypher import after copying the CSV files into Neo4j's import directory:

```cypher
LOAD CSV WITH HEADERS FROM 'file:///nodes.csv' AS row
MERGE (n:DefenseNode {id: row.id})
SET n.label = row.label, n.type = row.type,
    n.priority = row.priority, n.score = row.score;

LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row
MATCH (a:DefenseNode {id: row.source})
MATCH (b:DefenseNode {id: row.target})
MERGE (a)-[:RELATED {kind: row.relationship}]->(b);
```

For production graphs, convert `type` into explicit Neo4j labels and relation kinds after import rather than accepting arbitrary relation names from a CSV.
