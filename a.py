from collections import deque

goal_state = (
(1, 2, 3),
(4,0 ,5 ),
(6, 7, 8,))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def list_to_tuple(state):
    return tuple(tuple(row) for row in state)

def is_solved(state):
    return state == goal_state

def find_blank(state):
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c
    return -1, -1

def make_move(state, r, c, new_r, new_c):
    new_state = [list(row) for row in state]
    new_state[r][c], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[r][c]
    return list_to_tuple(new_state)

def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set([start_state])
    while queue:
        state, path = queue.popleft()
        if is_solved(state):
            return path
        r, c = find_blank(state)
        for dr, dc in moves:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_state = make_move(state, r, c, new_r, new_c)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [(r, c, new_r, new_c)]))
    return None

def display_puzzle(state):
    print("\n".join([" ".join(map(str, row)) for row in state]))
    print()

start_state = (
(1, 2, 3),
(4, 5, 6),
(7, 8, 0))
solution = bfs(start_state)

if solution:
    print("Solution found!")
    current_state = start_state
    display_puzzle(current_state)
    for move in solution:
        r, c, new_r, new_c = move
        current_state = make_move(current_state, r, c, new_r, new_c)
        display_puzzle(current_state)
else:
    print("No solution found.")