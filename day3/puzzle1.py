"""
Day 3 of AoC25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        lines = content.split()

    numbers=[]

    for line in lines:
        greater1 = algo_search(line)

        (linei,holder, lined) = line.partition(greater1)
        greater2 = algo_search(linei)
        greater3 = algo_search(lined)

        number1=int(greater2+greater1)
        number2=int(greater1+greater3)
        if int(greater3)==0: #Avoid getting results with a 0 at the end, like 90.
            number2=0


        numbers.append(max(number1,number2))

    sol=sum(numbers)
    print(len(numbers))
    print(numbers, sol)



def algo_search(line):
    greater=0

    for digit in line:
        if int(digit) > int(greater):
            greater = digit

    return str(greater)



if __name__ == '__main__':
    main()