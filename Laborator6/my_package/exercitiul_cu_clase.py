
from abc import ABC, abstractmethod
from enum import Enum


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


class Person(ABC):
    name: str
    age: int
    gender: Gender
    mother: "Adult" = None
    father: "Adult" = None
    all_people: list["Person"] = []

    def __init__(self, name: str, age: int, gender: Gender, mother=None, father=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.mother = mother
        self.father = father
        Person.all_people.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Numele nu poate fi gol!")
        self._name = value.strip()

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Varsta trebuie sa fie un numar pozitiv!")
        self._age = value

    @property
    def gender(self) -> Gender:
        return self._gender

    @gender.setter
    def gender(self, value: Gender):
        if not isinstance(value, Gender):
            raise ValueError("Genul trebuie sa fie male sau female!")
        self._gender = value

    """
    10*:
    Var1: lista cu evidenta a tuturor persoanelor
    Pro: nu pierd nicio persoana, usor de folosit
    Contra: ocupa memorie
    """
    @staticmethod
    def pass_year():
        for person in list(Person.all_people):
            person.age += 1
            if isinstance(person, Child) and person.age >= 18:
                new_adult = person.become_adult()
                idx = Person.all_people.index(person)
                Person.all_people[idx] = new_adult

    """
    Var2:
    O altă abordare ar fi fost parcurgerea recursiva incepand din Adult prin Children
    Pro: mai ok dpdv al memoriei
    Contra: risc de duplicare, daca sunt luati ambi parinti ai unui copil s ar putea sa i se creasca varsta de doua ori
    sau pentru persoanele care nu au parinti
    """


class Child(Person):
    def __init__(self, name: str, age : int, gender: Gender, mother=None, father=None):
        super().__init__(name, age, gender, mother, father)

    def become_adult(self) -> "Adult":
        new_age = max(self.age, 18)
        new_adult = Adult(self.name, new_age, self.gender, self.mother, self.father)
        if self.mother:
            index_mother = self.mother.children.index(self)
            self.mother.children[index_mother] = new_adult
        if self.father:
            index_father = self.father.children.index(self)
            self.father.children[index_father] = new_adult
        return new_adult


class Adult(Person):
    children: list

    def __init__(self, name: str, age: int, gender: Gender, mother=None, father=None):
        super().__init__(name, age, gender, mother, father)
        self.children = []

    def have_child_with(self, other: "Adult", child_name, child_gender: Gender = Gender.FEMALE):
        if self.gender == other.gender:
            raise ValueError("Parintii trebuie sa fie de sex opus!")

        if self.gender == Gender.FEMALE:
            mother = self
            father = other
        else:
            mother = other
            father = self
        new_child = Child(child_name, 0, child_gender, mother, father)
        self.children.append(new_child)
        other.children.append(new_child)
        return new_child

    def __add__(self, other):
        if not isinstance(other, Adult):
            raise TypeError("Sunt necesare doua obiecte de tip Adult!")
        return self.have_child_with(other, "Copil")



