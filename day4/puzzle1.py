"""
Day 4 AOC25
"""

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
    content = content.split()

    pos = search(content)
    frees = surroundings(pos)
    print(frees)
    print(len(frees))



def search(matrix):
    """Locate @s"""
    pos=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '@':
                pos.append([i,j])
    return pos


def surroundings(pos):
    """For each positions, check if the surroundings exists"""
    checks=[[-1,-1],[-1,0],[0,-1],[1,0],[1,1],[1,-1],[-1,1],[0,1]]
    frees=[]
    for pair in pos:
        comp=0
        for check in checks:
            aux_pos=[int(pair[0])+check[0], int(pair[1])+check[1]]
            if aux_pos in pos:
                comp+=1
        if comp<4:
            frees.append(pair)

    return frees


if __name__ == '__main__':
    main()