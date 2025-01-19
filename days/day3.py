def solve():
    
    import re

    file_contents = open('input/day3.txt').read()
    
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

    matches = re.findall(pattern, file_contents)

    ans = 0

    for m in matches:
        # print(m)
        
        numbers = [int(elem) for elem in m] # convert strings to int
        # print(numbers)
        result = numbers[0] * numbers[1]
        ans += result # add up to totalSum

    print(f'Part 1: {ans}')

    ### Part 2 
    # do() enables future instructions, don't() disables them 
    # enabled at start 

    # Strategy: start at beginning of text, scan for regex pattern, and store start index along with instruction
    # Do the same for do() and don't() patterns 
    
    # Find mul() matches with their positions
    instructions = [] 
    for match in re.finditer(pattern, file_contents):
        instructions.append(('mul',match.group(), match.start()))
        
    # Find do() matches with their positions 
    pattern = r"do\(\)"
    dos = [] 
    for match in re.finditer(pattern, file_contents):
        dos.append(('do',match.group(), match.start()))

    # Find don't() matches with their positions 
    pattern = r"don't\(\)"
    donts = [] 
    for match in re.finditer(pattern, file_contents):
        donts.append(('dont',match.group(), match.start()))
        
    all_instructions = instructions + dos + donts
    all_instructions_sorted = sorted(all_instructions, key=lambda x: x[2])

    ans2 = 0 
    enabled = True 
    for inst in all_instructions_sorted:
        if inst[0] == 'dont':
            enabled = False 
        elif inst[0] == 'do':
            enabled = True 
        elif (inst[0] == 'mul') & (enabled):
            numbers = [int(elem) for elem in inst[1].replace('mul(', '').replace(')','').split(',')] # convert strings to int
            result = numbers[0] * numbers[1]
            ans2 += result

    print(f'Part 2: {ans2}')