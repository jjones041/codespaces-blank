from project import olympian, gods_gender, gods_weapon

greek_gods = ["Zeus", "Hera", "Poseidon", "Demeter", "Hestia", "Hades"]
roman_gods = ["Jupiter", "Juno", "Neptune", "Ceres", "Vesta", "Pluto"]
gender = ["Male", "Female", "Male", "Female", "Female", "Male"]
weapons = ["thunderbolt", "scepter", "trident", "torch", "adamant rail", "bident"]

def test_olympian():
    assert olympian("Zeus") == "Roman Name: Jupiter"
    assert olympian("Hera") == "Roman Name: Juno"
    assert olympian("Poseidon") == "Roman Name: Neptune"
    assert olympian("Demeter") == "Roman Name: Ceres"
    assert olympian("Hestia") == "Roman Name: Vesta"
    assert olympian("Hades") == "Roman Name: Pluto"

def test_gods_gender():
    assert gods_gender("Y", "Zeus") == "Jupiter is a Male"

def test_gods_weapon():
    assert gods_weapon("thunderbolt", "Zeus") == "Correct! Jupiter's weapon of choice is a thunderbolt"