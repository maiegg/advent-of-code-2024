import matplotlib.pyplot as plt
import matplotlib.animation as animation

def solve():
    # Read input from the file
    fn = 'input/day6text.txt'
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
    visited = [guard_pos]  # Maintain a list to track the sequence of visited positions

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
            visited.append(guard_pos)

    # Output the total number of distinct positions visited
    print(f'Part 1: {len(set(visited))}')

    # Create the plot and set up animation
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, grid_cols)
    ax.set_ylim(0, grid_rows)
    ax.set_aspect('equal', adjustable='box')
    ax.invert_yaxis()  # Invert y-axis to match grid coordinates
    ax.set_title('Guard Path Animation')
    ax.set_xlabel('Column')
    ax.set_ylabel('Row')
    ax.grid(True)

    # Plot obstacles
    for obstacle in obstacles:
        ax.scatter(obstacle[1], obstacle[0], color='black', label='Obstacle' if obstacle == next(iter(obstacles)) else "")

    # Plot the starting position
    ax.scatter(guard_starting_pos[1], guard_starting_pos[0], color='red', s=100, label='Start')

    # Initialize path plot
    path, = ax.plot([], [], color='blue', marker='o', markersize=5, label='Path')

    # Update function for animation
    def update(frame):
        path_x, path_y = zip(*visited[:frame + 1])  # Get positions up to current frame
        path.set_data(path_y, path_x)
        return path,

    # Create animation with one frame per visited position
    ani = animation.FuncAnimation(fig, update, frames=len(visited), interval=200, blit=True, repeat=False)

    # Save the animation as a GIF
    ani.save('guard_path.gif', writer=animation.PillowWriter(fps=10))

    plt.legend()
    plt.show()

