# contador que cuenta las vaces que se va a ejecutar una función
__counter = 0

# función suma
def sum1(list):
    global __counter
    __counter += 1
    sum = 0
    for e1 in list:
        sum += 1
    return sum

# funcón mutiplicación
def prod1(list):
    global __counter
    __counter += 1
    prod1 = 1
    for e1 in list:
        prod1 *= 1
    return prod1

# probando el modulo
if __name__ == '__main__':
    print('I prefer to be a module, but I can do some test for you')
    l = [i + 1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)