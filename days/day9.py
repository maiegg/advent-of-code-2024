def build_disk_map(disk_map):
    """return the expanded disk representation as a list of characters"""
    disk = []
    file_id = 0

    for i in range(0, len(disk_map), 2):
        file_size = int(disk_map[i])
        if file_size > 0:
            disk.extend([str(file_id)] * file_size)  # Fill file blocks
        
        if i + 1 < len(disk_map):  # If there's a free space segment
            free_space_size = int(disk_map[i + 1])
            disk.extend(['.'] * free_space_size)  # Fill free space
        
        file_id += 1  # Increment file ID for the next file
    
    return disk


def compact_disk_old(disk):

    write_index = 0  # Where to place the next file block

    for read_index in range(len(disk)):
        if disk[read_index] != '.':  # If it's a file block
            disk[write_index], disk[read_index] = disk[read_index], '.'  # Swap file block left
            write_index += 1  # Move the write pointer

    return disk

def compact_disk(disk):
    first_empty_space_idx = ''.join(disk).find('.')  # Find the first empty space once

    # Iterate backwards through the list 
    for i in reversed(range(len(disk))):
        if i > first_empty_space_idx and disk[i] != '.':  
            # Move file block to the first empty space
            disk[first_empty_space_idx] = disk[i]
            disk[i] = '.'

            # Move `first_empty_space_idx` forward to the next empty space
            first_empty_space_idx += 1
            while first_empty_space_idx < len(disk) and disk[first_empty_space_idx] != '.':
                first_empty_space_idx += 1  

    return disk

    return disk
def calculate_checksum(disk):
    """Calculates checksum based on compacted disk."""
    checksum = 0

    for position, value in enumerate(disk):
        if value != '.':  # Ignore free space
            checksum += position * int(value)

    return checksum

def solve():
    fn = 'input/day9.txt'
    # input_string = open(fn).read().strip()
    input_string = "2333133121414131402"  # Test case

    # Main Execution
    
    disk = build_disk_map(input_string)
    # print(''.join(disk))

    disk = compact_disk(disk)
    # print(''.join(disk))

    checksum = calculate_checksum(disk)
    print("Part 1: Filesystem checksum:", checksum)
    
    ### Part 2 
    # Move only whole files
    # Process files in order of decreasing file id 
    