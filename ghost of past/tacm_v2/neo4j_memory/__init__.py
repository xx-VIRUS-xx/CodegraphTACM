"""neo4j_memory — Neo4j-backed active memory for TACM.

Replaces the in-memory LayeredGraph with a Neo4j-backed graph store that
supports:
  1. Full graph persistence (nodes, edges, signals)
  2. Real-time graph algorithms (PageRank, community detection, shortest paths)
  3. Persistent cross-query memory (exploration history, relevance decay)
  4. Dynamic knowledge graph updates (agent writes findings back)
"""
