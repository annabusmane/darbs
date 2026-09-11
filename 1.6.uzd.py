
def checkNumber(x):
    if x %2 == 0:
        print(f"Dotais skaitlis {x} ir pāra skaitlis")
    else:
        print(f"Dotais skaitlis {x} ir nepāra skaitlis")
        
x = int(input("Ievadiet skaitli: "))

checkNumber(x)
