def create_fibonacci_seq(count):
    if count == 1:
        nums.extend([0])
    if count == 2:
        nums.extend([0, 1])
    else:
        nums = [0, 1]
        for num in range(2, count):
            curr_num = nums[-1] + nums[-2]
            nums.append(curr_num)
    return nums

def locate_num(num, sequence):
    try:
        print(f"The number - {num} is at index {sequence.index(num)}")
    except ValueError:
        print(f"The number {num} is not in the sequence")


