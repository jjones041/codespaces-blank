import sys

def main():
    name = input("Name one of the original six Olympians (Greek name ONLY): ")
    olympian(name)
    answer = input("Was this the correct translation? (Y/N) ")
    gods_gender(answer, name)
    weapon = input("What is their weapon of choice? ")
    gods_weapon(weapon, name)


greek_gods = ["Zeus", "Hera", "Poseidon", "Demeter", "Hestia", "Hades"]
roman_gods = ["Jupiter", "Juno", "Neptune", "Ceres", "Vesta", "Pluto"]
gender = ["Male", "Female", "Male", "Female", "Female", "Male"]
weapons = ["thunderbolt", "scepter", "trident", "torch", "adamant rail", "bident"]


def olympian(name):
    if name in greek_gods:
        print("Translating...")
        g_name = greek_gods.index(name)
        r_name = roman_gods[g_name]
        print(f"Roman Name: {r_name}")
    else:
        sys.exit("Not an Olympian god!")

def gods_gender(answer, name):
    if answer == ("Y"):
        g_name = greek_gods.index(name)
        r_name = roman_gods[g_name]
        print(f"{r_name} is a {gender[g_name]}")
    else:
        sys.exit("Sorry, let me try again!")

def gods_weapon(weapon, name):
    if weapon in weapons and greek_gods.index(name) == weapons.index(weapon):
        g_name = greek_gods.index(name)
        r_name = roman_gods[g_name]
        print(f"Correct! {r_name}'s weapon of choice is a {weapon}")
    else:
        sys.exit("Wrong :(")


if __name__ == "__main__":
    main()