import numpy as np


def floyd_warshall(num_vertices, edges):
    dist_matrix = np.full((num_vertices, num_vertices), np.inf)
    np.fill_diagonal(dist_matrix, 0)
    
    for tail, head, weight in edges:
        dist_matrix[tail - 1, head - 1] = weight


    for k in range(num_vertices):
        print(f"Processing vertex {k+1}/{num_vertices}...")
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist_matrix[i][k] != np.inf and dist_matrix[k][j] != np.inf:
                    dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])
    
    if np.any(dist_matrix.diagonal() < 0):
        return None, True  # Negative cycle detected
    else:
        shortest_shortest_path = np.min(dist_matrix[dist_matrix != np.inf])
        return shortest_shortest_path, False


def load_graph(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_vertices, num_edges = map(int, lines[0].split())
        edges = [(int(line.split()[0]), int(line.split()[1]), float(line.split()[2])) for line in lines[1:]]
        return num_vertices, edges


def process_graph(file_path):
    print(f"Processing {file_path}...")
    num_vertices, edges = load_graph(file_path)
    shortest_path, has_negative_cycle = floyd_warshall(num_vertices, edges)
    if has_negative_cycle:
        print(f"Graph {file_path} has a negative cycle.")
    else:
        print(f"The shortest path in {file_path} is: {shortest_path}")


graph_files = ['g1.txt', 'g2.txt', 'g3.txt']


for graph_file in graph_files:
    process_graph(graph_file)


