def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    graph = {}
    n = int(input("Enter number of nodes: "))

    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = []
        for j in range(1, edges + 1):
            node = int(input("Enter edge {} for node {} : ".format(j, i)))
            graph[i].append(node)

    start_node = int(input("Enter the starting node: "))

    print("\nDFS Traversal:")
    dfs(graph, start_node, set())

    print("\n\nBFS Traversal:")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()
