def solve():
    
    import re

    text = open('input/day3.txt').read()
    
    # this regex is doing all the work - got help from reddit for this one 
    # per instruction, all mul() inputs are 1-3 digit numbers 
    # we look for strings matching "mul(" at beginnging : "mul/()"
    # followed by two 1-3 digit numbers separated by a comma: "(\d{1,3}),(\d{1,3})""
    # then followed by a literal close parens: "\)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # this works only because all the mul(123,123) instructions contain no other characters interpersed
    # (figuring this out by inspection of the input)
    # if the input didn't match the pattern mul(X,Y) literally, for example with inputs like mul(X, otherstuffY) - this fails 
    # You might be able to allow wildcards or spaces, but as there are a few incomplete mul instructions in the input, 
    # like mul(123, ...) with no second argument - this seems to return the wrong answer 
    # pattern = r"mul\(\s*(\d{1,3})\s*,\s*.*?\s*(\d{1,3})\s*\)"

    matches = re.findall(pattern, text)

    ans = 0

    for m in matches:
        # print(m)
        
        numbers = [int(elem) for elem in m] # convert strings to int
        # print(numbers)
        result = numbers[0] * numbers[1]
        ans += result # add up to totalSum

    print(f'Part 1: {ans}')