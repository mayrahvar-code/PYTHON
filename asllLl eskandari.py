from datetime import date

# Gereftane etelaate karbar
nam = input("Enter your first name: ")
nam_khanevadegi = input("Enter your last name: ")
sal_tavalod = int(input("Enter your birth year (Shamsi): "))

# Mohasebeye sen
sal_jari = date.today().year - 621
sen = sal_jari - sal_tavalod

# Namayeshe payame khosh amad
print("\nWelcome Message")
print("------------------------------")
print(f"Salaam {nam} {nam_khanevadegi}!")
print(f"Welcome to your {sen}th year! 🌸")
print("------------------------------")