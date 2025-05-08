import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                if neighbor not in visited:
                    new_cost = cost + 1
                    est_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (est_cost, new_cost, neighbor, path + [neighbor]))

    return None

# ---------- USER INPUT SECTION ----------
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the grid (0 for free space, 1 for obstacle):")
grid = []
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    grid.append(row)

start_x, start_y = map(int, input("Enter start position (row col): ").split())
goal_x, goal_y = map(int, input("Enter goal position (row col): ").split())

start = (start_x, start_y)
goal = (goal_x, goal_y)

# ---------- RUN A* ALGORITHM ----------
path = a_star(grid, start, goal)

print("\nShortest path using A*:")
if path:
    print(path)
else:
    print("No path found.")
