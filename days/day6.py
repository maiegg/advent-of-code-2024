def solve():
    # Read input from the file
    fn = 'input/day6.txt'
    grid = []
    with open(fn, 'r') as file:
        for line in file:
            grid.append(line.strip())

    # Get grid dimensions
    grid_rows = len(grid)
    grid_cols = len(grid[0])

    # Find the starting position of the guard and obstacles
    obstacles = set()
    guard_starting_pos = None
    guard_facing = 'up'  # Initial direction of the guard

    for i in range(grid_rows):
        for j in range(grid_cols):
            if grid[i][j] == '#':
                obstacles.add((i, j))
            elif grid[i][j] == '^':
                guard_starting_pos = (i, j)

    # Map directions to movements
    directions = {
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
        'left': (0, -1)
    }

    # Helper function to find the next position
    def find_next_pos(pos, facing):
        return (pos[0] + directions[facing][0], pos[1] + directions[facing][1])

    # Helper function to turn right
    def turn_right(current_facing):
        if current_facing == 'up':
            return 'right'
        elif current_facing == 'down':
            return 'left'
        elif current_facing == 'left':
            return 'up'
        elif current_facing == 'right':
            return 'down'

    # Simulate the guard's movement
    guard_pos = guard_starting_pos
    visited = set()
    visited.add(guard_pos)

    while True:
        next_pos = find_next_pos(guard_pos, guard_facing)

        # Check if the guard is still within the grid
        if not (0 <= next_pos[0] < grid_rows and 0 <= next_pos[1] < grid_cols):
            break

        # Check if the next position is an obstacle
        if next_pos in obstacles:
            # Turn right if blocked
            guard_facing = turn_right(guard_facing)
        else:
            # Move forward if not blocked
            guard_pos = next_pos
            visited.add(guard_pos)

    # Output the total number of distinct positions visited
    print(f'Part 1: {len(visited)}')
