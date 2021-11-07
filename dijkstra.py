#!/usr/bin/python3
'''
Finding the shortest path in a directed graph by Dijkstra's algorithm.
Graph is presented as a nested dictionary
{ 1: {2: 1, 3: 1}, 
  2: {3: 1, 5: 1}, 
  3: {4: 1, 6: 1}, 
  5: {6: 1}, 
  4: {1: 1, 7: 1}, 
  6: {4: 1}, 
  7: {}
}
'''

def add_edge(graph, nodes, source, target):
    if not source in graph:
        graph[source] = {}
        graph[source][target] = 1
    else:
        if not target in graph[source]:
            graph[source][target] = 1

    if not target in graph:
        graph[target] = {}

    nodes[source] = 1
    nodes[target] = 1
    return


def dijkstra_path(graph, nodes, source, target):
    inf = len(nodes) * 1000
    distanceto = {}
    for node in nodes.keys():
        distanceto[node] = inf
    distanceto[source] = 0
    previous = {}
    unseen = dict(nodes)
 
    while unseen:
        cur_node = None
        for node in unseen:
            if cur_node is None:
                cur_node = node
            elif distanceto[node] < distanceto[cur_node]:
                cur_node = node
        for child in graph[cur_node].keys():
            if graph[cur_node][child] + distanceto[cur_node]< distanceto[child]:
                distanceto[child]  = graph[cur_node][child] + distanceto[cur_node] 
                previous[child]=cur_node
            pass
        if cur_node == target:
            break
        unseen.pop(cur_node)

    path = []
    if distanceto[target] != inf:
        cur_node = target
        while cur_node != source:
            path.insert(0, cur_node)
            cur_node = previous[cur_node]
        path.insert(0,source)
    return path

g = {}
nodes = {}
add_edge(g, nodes, 1, 2)
add_edge(g, nodes, 1, 3)
add_edge(g, nodes, 2, 3)
add_edge(g, nodes, 2, 5)
add_edge(g, nodes, 3, 4)
add_edge(g, nodes, 3, 6)
add_edge(g, nodes, 4, 1)
add_edge(g, nodes, 4, 7)
add_edge(g, nodes, 5, 6)
add_edge(g, nodes, 6, 4)
add_edge(g, nodes, 3, 6)
print(g)

print(f"path 1->5: {dijkstra_path(g, nodes, 1, 5)}")
print(f"path 1->7: {dijkstra_path(g, nodes, 1, 7)}")
print(f"path 4->6: {dijkstra_path(g, nodes, 4, 6)}")
print(f"path 2->1: {dijkstra_path(g, nodes, 2, 1)}")
print(f"path 7->1: {dijkstra_path(g, nodes, 7, 1)}")
