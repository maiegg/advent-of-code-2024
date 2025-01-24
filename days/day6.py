def solveorig():
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

def solve():
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

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

    # Initialize plot and animation
    fig, ax = plt.subplots()
    ax.set_xlim(0, grid_cols)
    ax.set_ylim(0, grid_rows)
    ax.set_aspect('equal')
    ax.set_title('Guard Path Animation')

    # Plot obstacles
    for obstacle in obstacles:
        ax.add_patch(plt.Rectangle((obstacle[1], obstacle[0]), 1, 1, color='black'))

    # Initialize guard position and path
    guard_pos = guard_starting_pos
    visited = [guard_pos]

    # Function to update animation frame
    def update(frame):
        nonlocal guard_pos, guard_facing, visited
        next_pos = find_next_pos(guard_pos, guard_facing)

        # Check if the guard is still within the grid
        if not (0 <= next_pos[0] < grid_rows and 0 <= next_pos[1] < grid_cols):
            ani.event_source.stop()
            return

        # Check if the next position is an obstacle
        if next_pos in obstacles:
            # Turn right if blocked
            guard_facing = turn_right(guard_facing)
        else:
            # Move forward if not blocked
            guard_pos = next_pos
            visited.append(guard_pos)

        # Update plot with current guard position and path
        ax.scatter(guard_pos[1] + 0.5, guard_pos[0] + 0.5, color='blue')  # Plot current position
        for i, pos in enumerate(visited[:-1]):
            alpha = max(0.1, 1.0 - (len(visited) - i) / len(visited))  # Calculate fading alpha
            ax.scatter(pos[1] + 0.5, pos[0] + 0.5, color='blue', alpha=alpha)  # Plot fading path segment

    # Create animation
    ani = animation.FuncAnimation(fig, update, frames=None, repeat=False)
    plt.show()

    # Output the total number of distinct positions visited
    print(f'Part 1: {len(set(visited))}')

