"""
First puzzle of day 1 of AoC25
"""


def main():
    with open("input.txt", "r") as file:
        content = file.read()
        content1 = list()
        content1 = content.split()

        number = 50
        turns = 0
        print('We started at 50 and then:')
        for input in content1:
            addition, turns_extra = algo_password(input)
            print(addition)
            i = 0
            if addition > 0:
                # recorre exactamente 'addition' pasos
                while i < addition:
                    number += 1
                    if number == 100:
                        number = 0
                        turns += 1   # una vuelta completa hacia delante
                    i += 1

            else:
                # recorre exactamente 'abs(addition)' pasos hacia atrás
                while i > addition:
                    number -= 1
                    if number < 0:
                        number += 100
                        turns += 1   # una vuelta completa hacia atrás
                    i -= 1


            """
            number += addition
            print(f'Before applying anything we had {number}')
            if number == 0: #This should be up here cos it would count twice if 100 is hit perfectly
                turns += 1
            if number > 99:
                number += -100
                turns += 1
            elif number < 0:
                number += 100
                turns += 1
            print(f'Now we are at {number}, when added {addition}, and completed {turns} turns')
"""
            turns += turns_extra


    print(turns)
    print(number)



def algo_password(input):
    """Input is the number and letter. Now complete turns matter. I think Im gonna count these here"""
    turns = 0
    if len(input)>3:
        turns = int(input[1])
        input = input[0]+input[2:] #Each complete turn should add 1 per definition.
    if input[0] == "L":
        return -int(input[1:]), turns
    else:
        return int(input[1:]), turns


if __name__=='__main__':
    main()
