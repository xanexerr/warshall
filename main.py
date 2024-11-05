# Function to compute transitive closure using Warshall's algorithm
def warshall_algorithm(graph):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize the transitive closure matrix with the input graph
    transitive_closure = [[graph[i][j] for j in range(n)] for i in range(n)]
    
    # Apply Warshall's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If there's a path from i to k and from k to j, there is a path from i to j
                transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j])
    
    return transitive_closure

# Example usage
# 0 represents no edge, and 1 represents an 
n = int(input())
graph = [
]
for _ in range(n):
    row = []
    for c in range(n):
        row.append(int(input()))
    graph.append(row)
    
for i in range()
# Compute the transitive closure
closure = warshall_algorithm(graph)

# Print the result
print("Transitive Closure:")
for row in closure:
    print(row)