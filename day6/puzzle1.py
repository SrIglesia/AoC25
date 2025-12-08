"""
Docstring for AoC25.day6.puzzle1
"""

def main():

    with open('input.txt', 'r') as file:
        content = file.read().strip().split()

    divisor=len(content)//5
    print(divisor)
    operations=[]
    for i in range(divisor):
        operation = [content[i],content[i+divisor],content[i+2*divisor],content[i+3*divisor],content[i+4*divisor]]
        operations.append(operation)
        i+=5

    fresult = 0
    for operation in operations:
        if operation[-1] == '*':
            result = 1
            for j in range(len(operation[:-1])):
                result *= int(operation[j])
        else:
            result = 0
            for j in range(len(operation[:-1])):
                result += int(operation[j])

        fresult+=result
    print(fresult)



if __name__ == '__main__':
    main()