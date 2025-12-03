"""
Day 3 of AoC25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        lines = content.split()


    nums =  []
    for line in lines:
        nums.append(busq(line,12))
    
    print(sum(nums))


def algo_search(line):
    greater = "0"
    index = 0

    for i in range(len(line)):
        if line[i] > greater:
            greater = line [i]
            index = i

    return greater, index

def busq(line,reps=12):    
    num=''
    index = -1

    while len(num)<reps:
                
            n, index = algo_search(line)
            lineh=line
            while len(line[index:]) < reps-len(num):
                lineh=lineh.replace(n,'0')
                n, index = algo_search(lineh)
                
            line = line[index+1:]
            num+=n
    return int(num)

if __name__ == '__main__':
    main()