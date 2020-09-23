"""
Graph: Series of connected Nodes

Connection between nodes called edges or arcs

Connections can have a direction (arcs) or no direction (edges)

"""


graph = { 'A': ['B', 'C'],
          'B': ['C', 'D'],
          'C': ['D'],
          'E': ['F'],
          'F': ['C']
        }