import itertools
import numpy as np
import matplotlib.pyplot as plt
import math

def find_collinear_all_points_on_grid(tup1, tup2, num_rows, num_cols):
    r1, c1 = tup1
    r2, c2 = tup2

    res = set()
    
    # Handle vertical line case separately (avoid division by zero)
    if r1 == r2:
        for c in range(min(c1, c2), max(c1, c2) + 1):
            res.add((r1, c))
        return res, list(res)

    # Compute slope and intercept
    slope = (c2 - c1) / (r2 - r1)
    intercept = c1 - slope * r1

    for r in range(num_rows):
        for c in range(num_cols):
            if math.isclose(c, slope * r + intercept, abs_tol=1e-6):  # Avoid floating point issues
                res.add((r, c))

    return res, list(res)

def solve():
    fn = 'input/day8.txt'
    
    DEBUG = False

    # Create a dictionary of {freq : [ list of coordinate pairs ]}

    r = 0
    c = 0 

    antennae_pos = {} 
    

    D = open(fn).read().strip()
    for line in D.strip().split('\n'):
        for c in range(len(line)):
            if line[c] != '.':
                if line[c] not in antennae_pos.keys():
                    antennae_pos[line[c]] = []
                
                antennae_pos[line[c]].append(
                    (r,c)
                )

        r += 1 

    cols = c + 1 
    rows = r 
    
    if DEBUG:
        import matplotlib.pyplot as plt
        f,ax=plt.subplots()
        for _, positions in antennae_pos.items():
            for freq, positions in antennae_pos.items():
                for (r,c) in positions:
                    ax.annotate(xy=(c,r), text=freq, color='red')
                    ax.set_xticks(range(rows))
                    ax.set_yticks(range(cols))
                    ax.set_xlim([0, rows])
                    ax.set_ylim([cols, 0])
        plt.grid(True)
        plt.show()
    
    # print(antennae_pos)
    
    ########################################################################
    # Create an empty set to track antinode locations 
    ans = set() 
    import itertools 

    def in_bounds(r, c, rows, cols):
        if 0 <= r < rows and 0<= c < cols:
            return True
        return False 
    
    def find_collinear_points(tup1, tup2):
        r1, c1 = tup1
        r2, c2 = tup2

        if r1 == r2 and c1 == c2:
            return None 
        
        # Find direction and vector of p1 to p2, add to p2 
        dr = r2 - r1
        dc = c2 - c1 
        r3 = r2 + dr 
        c3 = c2 + dc 

        # Find direction and vector of p2 to p2, add to p1  
        dr = r1 - r2
        dc = c1 - c2
        r4 = r1 + dr 
        c4 = c1 + dc

        return (r3, c3), (r4, c4)
    
    for _, positions in antennae_pos.items():
        for (r1, c1), (r2, c2) in itertools.combinations(positions, 2):
            p3, p4 = find_collinear_points((r1,c1), (r2, c2))

            if DEBUG:
                # plt for debug 
                import matplotlib.pyplot as plt 
                f,ax=plt.subplots()
                ax.scatter(r1,c1, color='red')
                ax.scatter(r2,c2, color='red')
                ax.scatter(p3[0], p3[1], color='blue')
                ax.scatter(p4[0], p4[1], color='k')
                plt.show()

            if in_bounds(r=p3[0], c=p3[1], rows=rows, cols=cols):
                ans.add(p3)
            if in_bounds(r=p4[0], c=p4[1], rows=rows, cols=cols):
                ans.add(p4)
                
    print(f'Part 1: {len(ans)}')

    ########################################################################################################################
    ########################################################################################################################
    # Part 2: 

    import matplotlib.pyplot as plt 
    ans = set()
    lines = []

    for _, positions in antennae_pos.items():
        for (r1, c1), (r2, c2) in itertools.combinations(positions, 2):
            antinodes, line = find_collinear_all_points_on_grid(
                tup1=(r1, c1),
                tup2=(r2, c2),
                num_rows=rows,
                num_cols=cols
            )
            ans.update(antinodes)
            lines.append(line)

    if DEBUG:
        fig, ax = plt.subplots()
        for freq, positions in antennae_pos.items():
            for (r, c) in positions:
                ax.annotate(text=freq, xy=(c, r), color='red', fontsize=12, ha='center')
                ax.scatter(c, r, color='red', s=30)

        for (r, c) in ans:
            ax.scatter(c, r, color='blue', s=10)

        for line in lines:
            x_vals = [item[1] for item in line]  # Column index
            y_vals = [item[0] for item in line]  # Row index
            ax.plot(x_vals, y_vals, alpha=0.5)

        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.set_xlim([-1, cols])
        ax.set_ylim([rows, -1])  # Invert y-axis for correct display
        ax.grid(True)
        plt.savefig('day8 - test.png')

    print(f'Part 2: {len(ans)}')
