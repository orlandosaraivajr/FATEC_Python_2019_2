def soma(valor1, valor2):
    valor = valor1 + valor2
    if type(valor) is float:
        return round(valor, 2)
    return valor

assert(soma(2, 2) == 4)
assert(soma(2.0, 2.0) == 4.0)
assert(soma(1.1, 2.2) == 3.3)
assert(soma(2, 2.0) == 4.0)
assert(soma("Oi ", "Mundo") == "Oi Mundo")
assert(soma([1,2], [3,4]) == [1,2,3,4])


def soma_numeros(valor1, valor2):
    try:
        valor = valor1 + valor2
        x = complex(valor)
    except:
        return None
    return valor


assert(soma_numeros(2, 2) == 4)
assert(soma_numeros(2.0, 2.0) == 4.0)
# assert(soma_numeros(1.1, 2.2) == 3.3)
assert(soma_numeros(2, 2.0) == 4.0)
assert(soma_numeros("Oi ", "Mundo") == None)
assert(soma_numeros([1,2], [3,4]) == None)


def soma_numeros2(*valores):
    try:
        resultado=0
        for val in valores:
            resultado = resultado+val
        return resultado
    except:
        return None
    
assert(soma_numeros2(2,2) == 4)
assert(soma_numeros2(2,2,2) == 6)
assert(soma_numeros2(2,2,2,2) == 8)
assert(soma_numeros2(2.0,2.0) == 4.0)
assert(soma_numeros2(2,2.0) == 4.0)
assert(soma_numeros2("teste", "teste123") == None)
assert(soma_numeros2("teste", "test", "1234") == None)
assert(soma_numeros2("string", "str", 2,2, 3) == None)


def soma_numero3(*x):
    for item in x:
        if type(x[item]) is str:
            return "não é número"
        else:
            return sum(x)
assert (soma_numero3(1,1,3)==5)
assert (soma_numero3(2,4,"oi")=="não é número")
assert (soma_numero3(1,2)==3)