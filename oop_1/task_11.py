class Person:
    def __init__(self, name: str):
        self.name = name
        self.friends: list[Person] = []


def create_people() -> Person:
    firstPeople = Person("Bob")
    for i in range(4):

        if i == 0:
            new_people = Person("Mike")
        elif i == 1:
            new_people = Person("Job")
        elif i == 2:
            new_people = Person("Kate")
        else:
            new_people = Person("Rose")
        firstPeople.friends.append(new_people)
    return firstPeople


def show_people(people: Person):
    return people.friends


def main():
    print(show_people(create_people()))


main()
