x = int(input("Ievadiet pirmo skaitli: "))
y = int(input("Ievadiet otro skaitli: "))

summa = 0

for i in range(x, y + 1):
    summa += i

print(f"Visu skaitļu summa no {x} līdz {y} ir {summa} ")