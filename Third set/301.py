x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
#kod powyzej dziala poprawnie, dodatkowa uwaga: nie trzeba dawac średników

for i in "qwerty": if ord(i) < 100: print (i)
#kod powyzej nie zadziala, brakuje nowych lini oraz tabulatorów


for i in "axby": print (ord(i) if ord(i) < 100 else i)
#kod powyzej zadziala, jednak mozemy podniesc poiom jego czytelnosci poprzez przeniesienie "print" do kolejnej lini