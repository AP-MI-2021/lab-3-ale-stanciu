def printMenu():
    print ("1. Citire date")
    print ("2. Determinare cea mai lungă subsecvență in care toate numerele sunt pare")
    print ("3. Determinare cea mai lungă subsecvență in care media numerelor nu depășește o valoare citită")
    print ("4. Determinare cea mai lunga subsecventa in care toate numerele sunt divizibile cu k")
    print ("5. Iesire")

def read_list():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("L[" + str(i) + "]=")))
    return l

def ToateElementeleSuntPare(l):
    """
    Determina daca o lista are toate elementele nr. pare
    :param l: lista de nr. intregi
    :return: True, daca toate elementele din lista sunt nr. pare sau False, in caz contrar
    """
    for i in l:
        if i%2!=0:
            return False
    return True

def testToateElementeleSuntPare():
    assert ToateElementeleSuntPare([1,3,5]) == False
    assert ToateElementeleSuntPare([2,4,7]) == False
    assert ToateElementeleSuntPare([4,10,6]) == True

def get_longest_all_even(l):
    """
    Determina cea mai lungta subsecventa de elemente pare
    :param l: Lista de numere intregi
    :return: Cea mai lunga subsecventa de elemnte pare
    """
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if ToateElementeleSuntPare(l[i:j+1]) and len(subsecventaMax) < len(l[i:j+1]):
                subsecventaMax = l[i:j+1]
    return subsecventaMax

def test_get_longest_all_even():
    assert get_longest_all_even([]) == []
    assert get_longest_all_even([1,3,15,21]) == []
    assert get_longest_all_even([1,2,4,3,5,8]) == [2,4]

def MediaElementelor(l):
    """
    Calculeaza media aritmetica a tuturor elementelor din lista
    :param l: lista de nr. intregi
    :return: media aritmetica a elementelor listei
    """
    suma = 0
    for i in l:
        suma = suma + i
    media = suma/len(l)
    return media

def TestMediaElementelor():
    assert MediaElementelor([1,4,7]) == 4
    assert MediaElementelor([12]) == 12
    assert MediaElementelor([10,5]) == 7.5

def get_longest_average_below(l, average):
    """
    Determina cea mai lunga subsecventa in care toate elementele au media mai mica decat valoarea citita
    :param l: lista de nr. intregi
    :param average: valoarea citita (un numar intreg) cu care comparam media
    :return: Cea mai lunga subsecventa in care toate elementele din lista au media mai mica decat o valoare citita
    """
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if MediaElementelor(l[i:j + 1]) < average and len(subsecventaMax) < len(l[i:j + 1]):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_average_below():
    assert get_longest_average_below([2,4,3,55,23],5) == [1,2,3]
    assert get_longest_average_below([12],5) == []
    assert get_longest_average_below([5,3,10,6],10) == [5,3,10,6]

def EsteDiviziviblCuk(l,k):
    """
    Determina daca o lista are toate elementele divizibile cu k
    :param l: lista de nr. intregi
    :param k: valoarea citita cu care trebuie sa se divida elementele listei, un nr. intreg
    :return: True, daca toate elementele sunt divizibile cu k sau False, in caz contrar
    """
    for i in l:
        if i%k!=0:
            return False
    return True

def TestEsteDiviziviblCuk():
    assert EsteDiviziviblCuk([4,10,22,6],2) == True
    assert EsteDiviziviblCuk([4, 10, 23, 6], 2) == False

def get_longest_div_k(l,k):
    """
    Determina cea mai lunga subsecventa in care toate elementele sunt divizibile cu k
    :param l: lista de nr. intregi
    :param k: valoarea citita cu care trebuie sa se divida elementele listei, un nr. intreg
    :return: Cea mai lunga subsecventa in care toate elementele sunt divizibile cu k
    """
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if EsteDiviziviblCuk(l[i:j + 1], k) == True and len(subsecventaMax) < len(l[i:j + 1]):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax

def test_get_longest_div_k():
    assert get_longest_div_k([5,4,16,8,3],4) == [4,16,8]
    assert get_longest_div_k([2,6,15,20], 7) == []
    assert get_longest_div_k([3,9,18,6], 3) == [3,9,18,6]

def main():
    test_get_longest_all_even()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = read_list()
        elif optiune == "2":
            print(get_longest_all_even(l))
        elif optiune == "3":
            average = int(input("Dati valoarea cu care sa se compare media:"))
            print(get_longest_average_below(l, average))
        elif optiune =="4":
            k = int(input("Dati valoarea cu care doriti sa fie divizibile numelere: "))
            print(get_longest_div_k(l,k))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")
main()