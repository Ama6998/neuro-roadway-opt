import heapq
import time
import psutil

def heuristic(a, b):
    # Example: Manhattan or Euclidean distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path

def tag_interchanges(path, neuro_weights, threshold=1.5):
    tagged_path = []
    for node in path:
        weight = neuro_weights.get(node, 1)
        if weight < 1.1:
            tag = "low"
        elif weight < threshold:
            tag = "medium"
        else:
            tag = "high"
        tagged_path.append((node, tag))
    return tagged_path

def adaptive_a_star(graph, start, goal, neuro_weights):
    start_time = time.time()

    open_set = [(0, start)]
    cost = {start: 0}
    came_from = {}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            break
        visited.add(current)

        for neighbor, weight in graph.get(current, []):
            neuro_cost = weight * neuro_weights.get(neighbor, 1)
            new_cost = cost[current] + neuro_cost
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, neighbor))
                came_from[neighbor] = current

    path = reconstruct_path(came_from, start, goal)
    tagged_path = tag_interchanges(path, neuro_weights)

    end_time = time.time()
    mem = psutil.Process().memory_info().rss / 1024 / 1024

    print(f"Path found in {round(end_time - start_time, 4)} seconds")
    print(f"Memory used: {round(mem, 2)} MB")
    print("Tagged Path (Node, Interchange Stress):")
    for step in tagged_path:
        print(step)

    return tagged_path
