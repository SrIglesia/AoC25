"""
Day 3 of AoC25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        lines = content.split()

    numbers=[]

    line='234234234234278'
    line2='987654321111111'
    print(algo_search(line2))


def algo_search(line):
    greater = line[0]
    index = 0

    for i in range(len(line)):
        if line[i] > greater:
            greater = line [i]
            index = i

    return greater, index



if __name__ == '__main__':
    main()