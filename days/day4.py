def solve():
    fn = 'input/day4.txt'

    # Read input 
    grid = []
    with open(fn, 'r') as file:
        for line in file:
            grid.append(line.strip('\n'))

    # Traverse entire grid looking for "X" 
    # Search all directions and increment counter if necessary 
    # i = row indices, j = col indices 

    grid_cols = len(grid[0])
    grid_rows = len(grid) 
    
    word = 'XMAS'
    word_found_count = 0 

    directions = [
        (0, 1),   # Right
        (0, -1),  # Left 
        (1, 0),   # Down
        (-1, 0),  # Up
        (1, 1),   # Down and to the right 
        (-1, -1), # Up and to the left 
        (1, -1),  # Down and to the left 
        (-1, 1)   # Up and to the right 
    ]

    for i in range(grid_rows):
        for j in range(grid_cols):
            if grid[i][j] == word[0]:

                for direction in directions:
                    found = True # Assume that this is the start of a word to start, reset if broken later 
                    for k in range(1, len(word)):

                        next_i = i + direction[0]*k
                        next_j = j + direction[1]*k

                        # if out of bounds or next letter not found, break
                        if (
                            (next_i < 0 or next_i >= grid_rows or next_j < 0 or next_j >= grid_cols)
                            or 
                            (grid[next_i][next_j] != word[k])
                        ):
                            found = False
                            break
                        # else, keep looking (pass)

                    if found: # found will be True iff all letters found 
                        word_found_count += 1 

    print(f'Part 1: {word_found_count}')


