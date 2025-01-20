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

    # Part 2: "X-MAS"
    # X-MAS can appear with the M's starting in any 4 corners and continuing diagonally 
    # We require that both diagonals be filled with "MAS"
    
    # First approach: search for "MAS" just like above and try to link two diagonal instances of "MAS" (futzy)
    # Second approach: more efficient, search for A and then search outwards 

    word_found_count = 0 

    for i in range(grid_rows):
        for j in range(grid_cols):
            if grid[i][j] == 'A':

                # Two possible configurations for each diagonal
                # S in top right and M in bottom left OR vice versa (TR-BL)
                # S in top left and M in bottom right OR vice versa (TL-BR)

                bl_i, bl_j = i-1, j+1
                tl_i, tl_j = i-1, j-1
                tr_i, tr_j = i+1, j-1
                br_i, br_j = i+1, j+1

                # first check out of bounds; if so, pass
                if (
                    bl_i < 0 or bl_i >= grid_rows or 
                    bl_j < 0 or bl_j >= grid_cols or
                    tl_i < 0 or tl_i >= grid_rows or 
                    tl_j < 0 or tl_j >= grid_cols or
                    tr_i < 0 or tr_i >= grid_rows or 
                    tr_j < 0 or tr_j >= grid_cols or
                    br_i < 0 or br_i >= grid_rows or 
                    br_j < 0 or br_j >= grid_cols   
                ):
                    continue 
                elif (
                    (
                        # condition 1: the TR-BL diagonal is "MAS" in either direction 
                        (grid[bl_i][bl_j] == 'M' and grid [tr_i][tr_j] == 'S') 
                        or 
                        (grid[bl_i][bl_j] == 'S' and grid [tr_i][tr_j] == 'M')
                    )
                    and (
                        # condition 2: the TL-BR diagonal is "MAS" in either direction 
                        (grid[br_i][br_j] == 'M' and grid [tl_i][tl_j] == 'S') 
                        or 
                        (grid[br_i][br_j] == 'S' and grid [tl_i][tl_j] == 'M')                 
                    )
                ):
                    word_found_count += 1 

    print(f'Part 2: {word_found_count}')
