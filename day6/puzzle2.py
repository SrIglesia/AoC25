"""
Tengo que quitar los 0s de todas partes !
"""


def main():

    with open('input.txt', 'r') as file:
        content = file.read().strip().split()
    
    rows = prepare_rows(content, 5)
    #rows = ['79','84','562', '814','+']
    result = 0
    operations=[]
    for row in rows:
        ror = prepare_matrix(row)
        matrix = mount_matrix(ror)
        operation = prepare_calculations(matrix)
        print(operation)
        fresult=calculate_answer(operation)
        print(fresult)
        result+=fresult
    print(result)
    

def prepare_rows(content, n):
    divisor=len(content)//n
    operations=[]
    for i in range(divisor):
        operation = [content[i],content[i+divisor],content[i+2*divisor],content[i+3*divisor],content[i+4*divisor]]
        operations.append(operation)
        i+=n
    return operations

def prepare_calculations(matrix):
    operations=[]
    for i in range(4):
        operation = [matrix[0][-(i+1)],matrix[1][-(i+1)],matrix[2][-(i+1)],matrix[3][-(i+1)],matrix[4][-(i+1)]]
        operation = list(map(str,operation))
        if '0' in operation:
            operation.remove('0')

        operation = int(operation[0]+operation[1]+operation[2]+operation[3])#Cambiar esto
        operations.append(operation)
        i+=1
    if 0 in operations:
        operations.remove(0)
    operations.append(matrix[4][4])
    return operations

def calculate_answer(operation):
    fresult = 0
    print(operation)
    if operation[-1] == '*':
        result=1
        for number in operation[:-1]:
            result*=number
    else:
        result=sum(operation[:-1])

    return result

def prepare_matrix(row):
    #long = max(len(item) for item in row)
    long = 5
    r=[]

    #Rellenar los espacios al principio
    for item in row:
        i = 0 
        while len(item) < long:
            index = row.index(item)
            row.remove(item)
            item=' '+item
            row.insert(index, item)
    
    return row

def mount_matrix(row,n=5):
    matrix = []
    
    for i in range(n):
        line=[]
        for j in range(len(row[i])):

            if row[i][j] == ' ':
                line.append(0)
            else:
                line.append(row[i][j])
        matrix.append(line)

    return matrix

if __name__ == '__main__':
    main()