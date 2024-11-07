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

n = int(input("Enter the number of vertices: "))
graph = [[0] * n for _ in range(n)]
print("ใส่เลขเข้าไปในนี้ แล้วเว้นวรรค")
print('#ex : 1 1 1 1')
for i in range(n):
    row_input = input().strip()
    if row_input:
        row = list(map(int, row_input.split()))
        if len(row) != n:
            print("Invalid input. ใส่ใหม่อีกครั้ง")
            row_input = input().strip()
        graph[i] = row

closure = warshall_algorithm(graph)

print("Transitive")
for row in closure:
    for cell in row:
        print(cell, end=" ")
    print()