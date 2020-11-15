L = [3, 5, 4] ; L = L.sort()
#kod powyzej dziala, jednak nie tak jakbysmy tego oczekiwali. Do zmiennej L przypisujemy wynik funkcji sort, czyli None.
#jesli chcemy zwrocic posortowaną listę, powinnismy napisać samo L.sort()

x, y = 1, 2, 3 
#kod nie zadziala, poniewaz zbyt duzo wartosci chcemy przyisac do zbyt malej liczby zmiennych

X = 1, 2, 3 ; X[1] = 4
#kod powyzej tworzy tuple, w ktorym nie mozemy w taki sposob zmieniac wartosci. 
#jesli chcemy zmienic pierwszy element z tuple na 4 nalezy uzyc listy: X=[1,2,3] X[1]=4

X = [1, 2, 3] ; X[3] = 4
#kod powyzej nie zadziala, poniewaz wychodzimy poza zakres naszej listy, indeksy wynoszą kolejno: 0, 1, 2

X = "abc" ; X.append("d")
#kod powyzej nie zadziala, string nie posiada takiej metody jak append. 
#jesli chcemy dodac "d" do napisa "abc" wystarczy napisac: X +="d"

L = list(map(pow, range(8)))
#kod powyzej nie zadziala, funkcja pow potrzebuje conajmniej dwoch argumentow, a ma tylko jeden