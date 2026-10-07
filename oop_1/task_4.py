# задание просто показывает, что type может создавать классы программно, что очень круто для языка Python
# так как в этом языке все является объектом и type это тот же класс для создания классов
def create_objects(attr_object: list, name_class: str) -> type:
    i = 0
    return type(name_class, (), {attr: i + 1 for attr in attr_object})


def main():
    print(create_objects(["ad"], "User"))


main()
