"""
Day 2 of AoC 25
"""

def main():

    with open('input.txt', 'r') as file:
        content = file.read()
        parsedl=parse_input(content)

        fn = set()
        for pair in parsedl:
            nn = prepare_datasets(pair)
            fn.update(nn)

        fcount=sum(fn)

    print(fcount)

def prepare_datasets(input):
    """Takes two numbers separated by - and prepare the range of search, and divide in the middle the numbers"""
    numbers = input.split('-')
    nn=set()

    for number in range(int(numbers[0]), int(numbers[1])+1):
        snm=str(number)
        i=0

        while i < (len(snm)/2):
            if snm.count(snm[0:i+1])==len(snm)/(i+1):
                if len(snm)==1:
                    break
                nn.add(int(snm))
            i+=1
    return nn



def parse_input(input):
    """Gets the raw input and returns a list of pair of numbers in str format"""
    return input.split(',')




if __name__=='__main__':
    main()


