"""
Day 2 of AoC 25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        parsedl=parse_input(content)
        fcount = 0
        for pair in parsedl:
            invalids = prepare_datasets(pair)
            fcount += invalids

        print(fcount)

def prepare_datasets(input):
    """Takes two numbers separated by - and prepare the range of search, and divide in the middle the numbers"""
    numbers = input.split('-')
    print(numbers)
    invalids=0
    for number in range(int(numbers[0]), int(numbers[1])+1):
        snm=str(number)
        if len(snm)==1:
            pass
        lpart=snm[:int(len(snm)/2)]
        rpart=snm[int(len(snm)/2):]
        if lpart == rpart:
            invalids += number
    return invalids



def parse_input(input):
    """Gets the raw input and returns a list of pair of numbers in str format"""
    return input.strip().split(',')



if __name__=='__main__':
    main()


