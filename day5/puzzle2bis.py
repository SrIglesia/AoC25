"""
Day 5 of AoC25
"""


def main():
    with open('input.txt') as file:
        content = file.read().strip().split('\n\n')
        rgs,numbers = [group.split('\n') for group in content]


    print(rgs)
    intervals = []
    for r in rgs:
        intervals.append(sorted(map(int,(r.split('-')))))
    intervals.sort()

    merged = [intervals[0]]

    for curr_min, curr_max in intervals[1:]:
        last_min, last_max = merged[-1]

        # Se cruzan o tocan
        if curr_min <= last_max:
            merged[-1][1] = max(last_max, curr_max)
        else:
            merged.append([curr_min, curr_max])

    print(merged)
    
    sol=0
    for r in merged:
        sol+=r[1]-r[0]+1

    print(sol)

if __name__ == '__main__':
    main()