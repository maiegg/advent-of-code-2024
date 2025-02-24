def solve():
    fn = 'input/day1.txt'

    # Read file and organize into two lists 
    list1 = []
    list2 = [] 

    with open(fn, 'r') as file:
        for line in file:
            parts = line.split() # Split each line into two parts based on whitespace (default delimiter)
            if len(parts) == 2:
                # Convert parts to integers and append to respective lists
                num1 = int(parts[0])
                num2 = int(parts[1])
                list1.append(num1)
                list2.append(num2)   

    # Check: lists must be same length 
    if len(list1) != len(list2):
        print(f'Lists have two different lengths: {len(list1)} vs {len(list2)}')
        raise 

    # Sort lists
    list1sorted = sorted(list1)
    list2sorted = sorted(list2)

    def nth_smallest(lst, n):
        if n > 0 and n <= len(lst):
            return sorted(lst)[n - 1]  # Zero-based indexing
        else:
            raise ValueError(f'n={n} is out of range for list length {len(lst)}')

    # Find distance between Nth smallest number in each list 
    def distance(n: int, list1: list, list2: list):

        # Find index of nth smallest value in each list
        min1 = nth_smallest(lst=list1sorted, n=n)
        min2 = nth_smallest(lst=list2sorted, n=n)

        return abs(min1 - min2)

    ans = 0 
    for n in range(len(list1sorted)):
        ans += distance(
            n=n+1,
            list1=list1sorted,
            list2=list2sorted
        )

    print(f'part 1: {ans}')


    # Similarity Score:
    # times appeared in left list (list1) * times appeared in right list (list2) 
    ans2 = 0
    for i in list1:
        ans2 += (i * list2.count(i))
        
    print(f'part 2: {ans2}')
