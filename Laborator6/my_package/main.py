from exercitiul_cu_clase import Adult, Child, Gender, Person

if __name__ == "__main__":
    try:
        Adult("", -5, Gender.MALE)
        assert False, "Ar fi trebuit să arunce ValueError"
    except ValueError:
        print("Eroare prinsa!")

    tata = Adult("Ion", 30, Gender.MALE)
    mama = Adult("Maria", 28, Gender.FEMALE)
    copil = mama.have_child_with(tata, "Andrei")
    copil.age = 17
    copil2 = mama + tata
    print(f"Inainte: {copil.name} are {copil.age} ani si este {type(copil).__name__}")
    Person.pass_year()
    andrei_dupa_un_an = mama.children[0]
    print(f"Dupa 1 an: {andrei_dupa_un_an.name} are {andrei_dupa_un_an.age} ani si este {type(andrei_dupa_un_an).__name__}")
