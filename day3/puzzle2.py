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

    num=[]
    index = 0
    i = 0
    while len(num)<12:
        n, index = algo_search(line2[index+i])
        num.append(int(n))
        i+=1
    print(num)

    greater, index = algo_search(line2)
    greater2, index2 = algo_search(line2[index+1:])
    greater3, index3 = algo_search(line2[index+2:])
    print(greater,greater2,greater3, num)


def algo_search(line):
    greater = "0"
    index = 0

    for i in range(len(line)):
        if line[i] > greater:
            greater = line [i]
            index = i

    return greater, index



if __name__ == '__main__':
    main()