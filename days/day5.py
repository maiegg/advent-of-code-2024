def solve():
    fn = 'input/day5.txt'

    # Read input 
    grid = []
    with open(fn, 'r') as file:
        data = file.read()

    # Split the data into lines
    parts = data.split("\n\n")

    # First part of update: rules
    # Second part of update (after blank line): updaets 
    rules = [tuple(map(int, rule.split('|'))) for rule in parts[0].strip().splitlines()]
    updates = [list(map(int, update.split(','))) for update in parts[1].strip().splitlines()]

    def is_update_valid(update, rules):
        # "update" = list of numbers 
        # "rules" list of tuples 

        # Relevant rules = those in which BOTH pages referenced are contained in the update 
        relevant_rules = [(a,b) for a, b in rules if a in update and b in update]
        
        # Create a lookup of {value: idx} for all the values in update 
        pos_lookup = {value: idx for idx, value in enumerate(update)}
        
        # Check each rule to see if the update proposes an order that would violate a rule
        # If any such violations are found, return false (invalid update); else true (valid update)
        for a,b in relevant_rules:
            if pos_lookup[a] >= pos_lookup[b]:
                return False 
        return True 

    ans = 0 
    for update in updates:
        if is_update_valid(update, rules):
            ans += update[len(update) // 2]
        
    print(f'Part 1: {ans}')

    # Part 2: 
    def make_update_valid(update, rules):
        # Relevant rules = those in which BOTH pages referenced are contained in the update 
        relevant_rules = [(a,b) for a, b in rules if a in update and b in update]
        
        # Create a lookup of {value: idx} for all the values in update 
        pos_lookup = {value: idx for idx, value in enumerate(update)}
        
        while not is_update_valid(update, relevant_rules):
            for a,b in relevant_rules:
                if pos_lookup[a] >= pos_lookup[b]:
                    update[pos_lookup[a]] = b
                    update[pos_lookup[b]] = a 

                    old_a_pos = pos_lookup[a]
                    old_b_pos = pos_lookup[b]
                    pos_lookup[a] = old_b_pos
                    pos_lookup[b] = old_a_pos

        return update 
      
    # Iterate through the updates
    ans = 0
    for update in updates:
        if is_update_valid(update, rules):
            pass
            # ans += update[len(update) // 2]
        else:
            # print('bad update:',update)
            update_fixed = make_update_valid(update, rules)
            ans += update_fixed[len(update_fixed) // 2]
            
    print(f'Part 2: {ans}')