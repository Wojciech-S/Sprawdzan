#1. Struktury danych w Pythonie to: listy, słowniki, tuple (krotki) i zbiory.

#2. Mutowalne są następujace struktury: listy, słowniki i zbiory
# (choć słyszałem, że są pewne typy zbiorów, które są niemutowalne, ale o nich nie mówiliśmy)

#4. Masz słownik
	#	zrodla = {"a": 10, "b":30}
#Jak bezpiecznie wybrać z tego słównika wartość i przypisać ją do zmiennej, to by nie był rzucony błąd?
#Np. chcesz sprawdzić dla wartości "c", której nie ma w słowniku

zrodla = {"a": 10, "b" : 30}
pytanie = input("Podaj dowolną literę alfabetu, aby sprawdzić, czy jest ona w słowniku: ")
if pytanie in zrodla:
    print(zrodla[pytanie])
else:
    print("Brak")

#5. Zdefiniuj funkcję foo, która przyjmie dowolną liczbę argumentów pozycyjnych i kluczowych
   #funkcja ma wypisać na ile ich jest

def foo(args, kwargs):
    print(f"pozycyjnych {len[args]} \n kluczowych {len[kwargs]}")
    return