def solve():
    
    fn = 'input/day2.txt'

    # Read input 
    levels = []
    with open(fn, 'r') as file:
        for line in file:
            parts = line.split() # Split each line into parts based on whitespace (default delimiter)
            parts = [int(i) for i in parts]
            levels.append(
                parts
            )

    # Analyze each level
    # "Safe" criteria: all increasing or decreasing, step size 1 or 2
    def check_list(lst):
        # Check if the list is monotonic (increasing or decreasing)
        is_increasing = all(lst[i] < lst[i+1] for i in range(len(lst) - 1))
        is_decreasing = all(lst[i] > lst[i+1] for i in range(len(lst) - 1))
        
        # Check if all step sizes are <= 2
        valid_steps = all(abs(lst[i] - lst[i+1]) <= 3 for i in range(len(lst) - 1))
        
        # Return TRUE if both conditions are met
        return (is_increasing or is_decreasing) and valid_steps

    ans = 0 
    for level in levels:
        if check_list(level) == True:
            ans += 1

    print(f'Part 1: {ans}')

    # Part 2: Problem Dampener 
    def can_make_safe(lst):
        def is_safe(lst):
            # Check if the list is monotonic (increasing or decreasing)
            is_increasing = all(lst[i] < lst[i+1] for i in range(len(lst) - 1))
            is_decreasing = all(lst[i] > lst[i+1] for i in range(len(lst) - 1))
            # Check if all step sizes are <= 2
            valid_steps = all(abs(lst[i] - lst[i+1]) <= 3 for i in range(len(lst) - 1))
            # Return True if both conditions are met
            return (is_increasing or is_decreasing) and valid_steps

        # Check if the list is already safe
        if is_safe(lst):
            return True

        # Try removing one level and check if it becomes safe
        for i in range(len(lst)):
            modified_lst = lst[:i] + lst[i+1:]  # Remove the ith element
            if is_safe(modified_lst):
                return True

        # If no removal makes it safe, return False
        return False

    print(f'Part 2: {sum([can_make_safe(item) for item in levels])}')