def solve():
    fn = 'input/day8test.txt'
    
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
                        
    print(antennae_pos)
    ########################################################################
    # Create an empty set to track antinode locations 
    ans = set() 
    import itertools 

    for freq, positions in antennae_pos.items():
        for (r1, c1), (r2, c2) in itertools.combinations(positions, 2):
            1==1 


    # Every pair of antennae will have 2 antinodes; if these are in-bounds, add them to the set 
