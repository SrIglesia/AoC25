"""
Day 5 of AoC25
"""


def main():
    with open('input.txt') as file:
        content = file.read().strip().split('\n\n')
        ranges,numbers = [group.split('\n') for group in content]

    ranges = def_ranges(ranges)
    count = check_in(numbers, ranges)
    print(count)

def def_ranges(input):
    ran=set()
    ran.add([list(range(int(line.split('-')[0]),int(line.split('-')[1])+1)) for line in input])
    return ran[0]

def check_in(inputs,ranges):
    count=0
    fresh=[]
    for i in inputs:
        for range in ranges:
            if int(i) in range and i not in fresh:
                count += 1
                fresh.append(i)
                print(f'Found fresh {i} in {range}')
    return count



if __name__ == '__main__':
    main()