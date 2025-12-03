"""
Day 3 of AoC25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        lines = content.split()


    line = '8977564321'
    line=replace(line,2)
    print(line)
    print(len(line))

def replace(line: str,n):
    i=0
    lineh=line
    while len(line)>n:
        lineprev=line
        line=line.replace(str(i+1),'')
        print(line)
        i+=1

        if len(line)<n:
            line=lineprev

            while len(lineprev)<n:
                if lineh[-i]!=lineprev[-i]:
                    lineprev=lineprev[:-(i+1)]+lineh[-i]+lineprev[-i]
                    print(lineprev)
                    i+=1
            return line

    return line



if __name__ == '__main__':
    main()