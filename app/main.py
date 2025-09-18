class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])

    for person in people:
        instance = Person.people[person["name"]]
        if person.get("wife"):
            instance.wife = Person.people[person["wife"]]
        if person.get("husband"):
            instance.husband = Person.people[person["husband"]]

        person_list = []

    for person_dict in people:
        person_list.append(Person.people[person_dict["name"]])
    return person_list
