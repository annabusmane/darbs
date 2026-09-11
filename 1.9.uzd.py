x = int(input("Ievadiet pirmo skaitli: "))
y = int(input("Ievadiet otro skaitli: "))

print(f"Pāra skaitļi diapazonā no {x} līdz {y}: ")

for i in range(x, y + 1):

  if i %2 == 0:
    print(i)