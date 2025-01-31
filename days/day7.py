def solve():
    # Read input from the file
    fn = 'input/day7test.txt'
    data = {}
    with open(fn, 'r') as file:
        for line in file:

            k = int(line.split(': ')[0])
            v = [int(i) for i in line.split(': ')[1].split(' ')]
            data[k] = v
    
    import itertools 

    def generate_operator_combinations(n):
        operators = ['+','-','*','/']
        return list(itertools.product(operators, repeat=n-1))

    def evaluate_expression(numbers, operators):
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == '+':
                result += numbers[i+1]
            elif operators[i] == '-':
                result -= numbers[i+1]
            elif operators[i] == '*':
                result *= numbers[i+1]
            elif operators[i] == '/':
                if numbers[i+1] == 0:
                    return float('inf')
                result /= numbers[i+1]

        return result

    
    def count_ways(target, numbers):
        operator_combinations = generate_operator_combinations(len(numbers))
        count = 0 
        
        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            
            if result == target:
                count += 1 

        return count 
    
    ans = 0 
    for (k, v) in data.items():
        # print(k,v, count_ways(target=k, numbers=v))
        ans += count_ways(target=k, numbers=v)
    print(f'Part 1: {ans}')