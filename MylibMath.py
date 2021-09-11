from numpy import radians


def sub (vector1, vector2):
    newVector = []
    if len(vector1) != len(vector2):
        return ArithmeticError("Las matrices no son del mismo tamaño")
    else:
        for x in range(len(vector1)):
            newVector.append(vector1[x]-vector2[x])
        return newVector


def punto (vector1, vector2):
    if len(vector1) != len(vector2):
        return ArithmeticError("Las matrices no son del mismo tamaño")
    else: 
        total = 0 
        for x in range(len(vector1)):
            total += vector1[x] * vector2[x]
        return total


def cross(vector1, vector2):
    if len(vector1) == 3 & len(vector2) == 3:
        i = vector1[1]*vector2[2] - vector2[1]*vector1[2]
        j = vector1[0]*vector2[2] - vector2[0]*vector1[2]
        k = vector1[0]*vector2[1] - vector2[0]*vector1[1]
        return [i, -j, k]
    if len(vector1) == 2 & len(vector2) == 2:

        k = vector1[0]*vector2[1] - vector2[0]*vector1[1]
        return [k]
    else:

        return ArithmeticError("No puede hacerse")


def matrizInv(matriz):
    n = len(matriz)
    m = matriz

    for i in range(n):
        for j in range(n):
            if i == j:
                m[i].append(1)
            else:
                m[i].append(0)

    for i in range(n):
        if m[i][i] == 0.0:
            ArithmeticError("No puede hacerse")
        
        for j in range(n):
            if i != j:
                ratio = m[j][i]/m[i][i]

                for k in range(2*n):
                    m[j][k] = m[j][k] - ratio * m[i][k]

    for i in range(n):
        divisor = m[i][i]
        for j in range(2*n):
            m[i][j] = m[i][j]/divisor

    resultado = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n, 2*n):
            resultado[i].append(m[i][j])

    
    return resultado



def Deg2rad(data):
    pi = 22/7
    deg = data 
    radian = deg * (pi/180)
    return radian

def Pi ():
    return 22/7 


def Matrix(data):
    return [[data]]


def norm(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

