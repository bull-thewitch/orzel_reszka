import random
import time

computer = 0
user = 0

while True:
    print("Zagrajmy w orzeł i reszka. Rzucaj pierwszy, człowieku!\nWybierz 'o'rzeł / 'r'eszka: ")
    u = input().lower()
    if u == 0:
        break
    elif u == "o":
        u = "orzeł"
    elif u == "r":
        u = "reszka"
    else:
        print("Dokonaj właściwego wyboru:\no - orzeł\nr - reszka\n0 - koniec gry")
        continue

    cast = random.choice(["orzeł", "reszka"])

    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)
    
    print("Wynik rzutu: ", cast)

    if u == cast:
        user += 1
    else:
        computer += 1
    
    print("Wyniki łącznie.")
    print("Uzytkownik: ", user)
    print("Komputer: ", computer)





   
          