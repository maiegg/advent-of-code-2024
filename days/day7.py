def solve3():
    print('v2')
    fn = 'input/day7.txt'

    equations = dict()
 
    def canGenerateResult(currSum, idx, result, equation):
        if idx == len(equation):
            if currSum == result:
                return True
            else:
                return False
        return (canGenerateResult(currSum + equation[idx], idx + 1, result, equation) or
                canGenerateResult(currSum * equation[idx], idx + 1, result, equation))


    def calibrationResult(equations: dict) -> int:
        totalCalibrationResult = 0
        for result, equation in equations.items():
            if canGenerateResult(equation[0], 1, result, equation):
                totalCalibrationResult += result
        return totalCalibrationResult
    
    file_path = fn
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            key = int(line.split(":")[0])
            val = [int(num) for num in line.split(":")[1].strip().split(" ")]
            equations[key] = val
    print(calibrationResult(equations))

def solve():
    # Read input from the file
    fn = 'input/day7.txt'
    data = {}
    with open(fn, 'r') as file:
        for line in file:

            k = int(line.split(': ')[0])
            v = [int(i) for i in line.split(': ')[1].split(' ')]
            data[k] = v
    
    import itertools 

    def generate_operator_combinations(n):
        # generate a lit of the possible operator combinations based on how many "spaces between numbers" (ie, len(v) - 1) there are
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
    
    ans = 0 
    for (k, v) in data.items():
        ans += targetIfSolvable(target=k, numbers=v)

    print(f'Part 1: {ans}')




