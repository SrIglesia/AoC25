"""
Day 5 of AoC25
"""


def main():
    with open('input2.txt') as file:
        content = file.read().strip().split('\n\n')
        rgs,numbers = [group.split('\n') for group in content]

    #count = check_in(numbers, rgs)

    i = 0
    lsaux=[]
    for i in range(len(rgs)):
        #Comparar los límites de cada espacio. Si se cruzan unirlos, si no meter ambos a la lista:
        rgmin, rgmax = sorted(rgs[i].split('-'))
        rgmax = int(rgmax)
        rgmin = int(rgmin)
        #Doy la primera condición en el primer espacio.
        if i == 0:
            lista=[int(rgmin), int(rgmax)]
            lsaux.append(lista)



        else:
            listas=[]
            for k in range(0, len(lsaux) + 1): #Al comparar con todas, aunque dos se cruzen, me esta añadiendo porque con la otra que compara no se cruza.
                lista=lsaux[k]
                print(f'Este es el limite menor que probamos, {rgmin}, el limite mayor, {rgmax}, contra esta lista, {lista[0]}, {lista[1]}')
                if rgmin<=lista[0] and rgmax>=lista[1]:
                    lsaux.remove(lista)

                    lista=[rgmin, rgmax]
                    print('Condicion 1')
                    listas.append(lista)
                    print(listas)

                elif rgmin<lista[0] and rgmax<lista[1]:
                    lsaux.remove(lista)
                    lista=[rgmin, lista[1]]
                    print('Condicion 2')
                    listas.append(lista)
                    print(listas)

                
                elif rgmin>lista[0] and rgmax>lista[1] and rgmin<lista[1]:
                   lsaux.remove(lista)
                   lista=[lista[0], rgmax]
                   print('Condición 3')
                   listas.append(lista)
                   print(listas)
                
                elif rgmin<lista[0] and rgmax<lista[0] or rgmin>lista[1] and rgmax>lista[1]:
                    print('Condición 4')
                    listas.append([rgmin, rgmax])
                    print(listas)

            j=0
            maxim=[0,0]
            for j in range(len(listas)):
                if listas[j][1]-listas[j][0]>maxim[1]-maxim[0]:
                    maxim = listas[j]
                j+=1
            lsaux.append(maxim)
            k+=1

            print(f'Esta lista queda en cada iteración completa {lsaux}')

    print(lsaux)


    #count = check_in(minimo, maximo, rgs)
    #print(count)

def check_in(minimo, maximo ,rgs):
    count=0
    fresh=[]
    i = minimo
    while i < maximo +1:
        for rg in rgs:
            rg = rg.split('-')
            rg.sort()
            i = int(i)
            if i >= int(rg[0]) and i <= int(rg[1]) and i not in fresh:
                count += 1
                fresh.append(i)
        i+=1
        print(i)
    return count




if __name__ == '__main__':
    main()