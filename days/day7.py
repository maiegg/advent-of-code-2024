def solve():
    # Read input from the file
    fn = 'input/day7.txt'

    def is_valid(target, ns, p2):
        if len(ns) == 1:
            return ns[0] == target
        if is_valid(target, [ns[0] + ns[1]] + ns[2:], p2):
            return True
        if is_valid(target, [ns[0]*ns[1]] + ns[2:], p2):
            return True
        if p2 and is_valid(target,[int(str(ns[0]) + str(ns[1]))] + ns[2:], p2):
            return True
        return False
    
    p1 = 0
    p2 = 0
    D = open(fn).read().strip()
    for line in D.strip().split('\n'):
        target, ns = line.strip().split(':')
        target = int(target)
        ns = [int(x) for x in ns.strip().split()]
    
        if is_valid(target, ns, p2=False):
            p1 += target
        if is_valid(target, ns, p2=True):
            p2 += target

    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
    # Above solution is easier to extend for part 2; below is my original for part 1. 
    # I had a bug in the file parsing that kept me stuck for a while, but core logic was correct 

    import itertools 

    def generate_operator_combinations(n):
        # generate a lit of the possible operator combinations based on how many "spaces between numbers" (ie, len(v) - 1) 
        operators = ['+','*']
        return list(itertools.product(operators, repeat=n-1))

    def evaluate_expression(numbers, operators):
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i+1]
            elif operators[i] == '*':
                result = result * numbers[i+1]
        return result
    
    def targetIfSolvable(target, numbers):
        operator_combinations = generate_operator_combinations(len(numbers))    

        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == target:
                return int(target)

        return 0
    

    # Read input from the file
    ans = 0 
    
    D = open(fn).read().strip()
    for line in D.strip().split('\n'):
        target, ns = line.strip().split(':')
        target = int(target)
        ns = [int(x) for x in ns.strip().split()]
        ans += targetIfSolvable(target=target, numbers=ns)

    print(f'Part 1 (orig): {ans}')