#!/usr/bin/python3.5

def main(a, c, m, x0, n):

    numeros = []
    xn = x0
    numeros.append(x0)

    for i in range(1, n):
        numero = (a * xn + c) % m

        if numero in numeros:
            print("{0}: {1}".format(i, numero))
            print("El generador tiene un peiodo de {0}".format(i))
            break
        else:
            numeros.append(numero)
            xn = numero
        print("{0}: {1}".format(i, numero))

    print("{0} numeros generados".format(n))


def nextNumber(x0):
    x1 = x0 ** 2
    x1 = str(x1)
    #print x1Exp
    aux = 0
    while len(x1) > 4:
        if aux==0:
            x1.pop(len(x1)-1)
            aux = 1
        else:
            x1.pop(0)
            aux = 0
    x1=''.join(map(str, x1))
    x1 = int(x1)
    #print x1
    #print x1Exp
    return x1


def cuadrado(x0):
    cond = 0
    i = 0
    numbers = [x0]

    while cond == 0:
        numbers.append(nextNumber(numbers[i]))
        i = i + 1
        if len(numbers) != len(set(numbers)):
        #if i == 5:
            cond = 1

    print (len(numbers))
    print (numbers)