def termina_com(texto, sufixo):
    return texto.endswith(sufixo)
#    if texto.endswith(sufixo):
#       return True
#    return False

assert(termina_com('fatec','tec') == True)
assert(termina_com('google','g') == False)
assert(termina_com('fatec','g') == False)
assert(termina_com('andando','ndo') == True)

def texto_interno(texto, subtexto):
    if subtexto in texto:
        return True
    return False

assert(texto_interno('fatec','tec')==True)
assert(texto_interno('google','g')==True)
assert(texto_interno('fatec','g')==False)

def texto_interno2(texto, contem):
    try:
        if texto.index(contem) >= 0:
            return True
    except:
        return False
    
assert(texto_interno2('fatec','tec')==True)
assert(texto_interno2('google','g')==True)
assert(texto_interno2('fatec','g')==False)

def text_interno3(txt, sub):
    return txt.find(sub) > -1

assert(text_interno3('fatec','tec'))
assert(text_interno3('google','g'))
assert(not text_interno3('fatec','g'))


def frequencia(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    return letter_dict


assert(frequencia('ovo') == {'o': 2, 'v': 1})
assert(frequencia('araras') == {'a': 3, 'r': 2, 's': 1})
assert(frequencia('pindamandapio') == {'p': 2, 'i': 2, 'n': 2, 'd': 2, 'a': 3, 'm': 1, 'o': 1})


def freq(palavra):
    dic = {}
    for l in palavra:
        dic[l] = palavra.count(l)
    return dic

assert(freq('ovo') == {'o': 2, 'v': 1})
assert(freq('araras') == {'a': 3, 'r': 2, 's': 1})
assert(freq('pindamandapio') == {'p': 2, 'i': 2, 'n': 2, 'd': 2, 'a': 3, 'm': 1, 'o': 1})

from collections import Counter
def freq1(texto):
    return Counter(texto)

assert(freq1('ovo') == {'o': 2, 'v': 1})
assert(freq1('araras') == {'a': 3, 'r': 2, 's': 1})
assert(freq1('pindamandapio') == {'p': 2, 'i': 2, 'n': 2, 'd': 2, 'a': 3, 'm': 1, 'o': 1})













    