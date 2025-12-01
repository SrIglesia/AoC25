"""
First puzzle of day 1 of AoC25
"""


def main():
    with open("input.txt", "r") as file:
        content = file.read()
        content1 = list()
        content1 = content.split()

        number = 50
        count = 0

        for input in content1:
            number += algo_password(input)
            if number > 99:
                number += -100
            elif number < 0:
                number += 100
            if number == 0:
                count += 1

    print(number)
    print(count)



def algo_password(input):
    """Input is the number and letter"""
    if len(input)>3:
        input=input[0]+input[2:] #They are complete turns, so doesn't matter this number.
    if input[0] == "L":
        return -int(input[1:])
    else:
        return int(input[1:])


if __name__=='__main__':
    main()
