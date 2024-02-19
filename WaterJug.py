from collections import deque

def bfs(capacities, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        jug1, jug2 = queue.popleft()

        if jug1 == target or jug2 == target:
            return jug1, jug2

        visited.add((jug1, jug2))

        # Generate all possible next states
        next_states = [(0, jug2), (jug1, 0), (capacities[0], jug2), (jug1, capacities[1]), 
                       (min(jug1 + jug2, capacities[0]), max(0, jug1 + jug2 - capacities[0])), 
                       (max(0, jug1 + jug2 - capacities[1]), min(jug1 + jug2, capacities[1]))]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

    return None

def dfs(capacities, target):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        jug1, jug2 = queue.pop()

        if jug1 == target or jug2 == target:
            return jug1, jug2

        visited.add((jug1, jug2))

        # Generate all possible next states
        next_states = [(0, jug2), (jug1, 0), (capacities[0], jug2), (jug1, capacities[1]), 
                       (min(jug1 + jug2, capacities[0]), max(0, jug1 + jug2 - capacities[0])), 
                       (max(0, jug1 + jug2 - capacities[1]), min(jug1 + jug2, capacities[1]))]

        for state in next_states:
            if state not in visited:
                queue.append(state)
                visited.add(state)

    return None

# Example usage
if __name__ == "__main__":
    capacities = (4, 3)  # Jug capacities
    target = 2  # Target amount of water

    final_state = bfs(capacities, target)

    if final_state:
        print("Target amount of water is achievable.")
        print("Final state:", final_state)
    else:
        print("Target amount of water is not achievable.")
