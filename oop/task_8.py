# Моя нелюбимая тема, она связана также с ссылками и все такое, но логика красивая тут
class Node:
    def __init__(self, info: str):
        self.info = info
        self.next = None


def create_objects(n: int) -> Node:
    count = 1
    first_object = Node(f"объект {count}")
    current_object = first_object
    if n > 1:
        for i in range(n - 1):
            count += 1
            new_object = Node(f"объект {count}")
            current_object.next = new_object
            current_object = new_object

    elif n == 1:
        return first_object
    else:
        print("n > 0")
        return None
    return first_object


def show_chain(first_object: Node | None):
    current_object = first_object

    while current_object is not None:
        print(
            f"{current_object.info} "
            f"-> {current_object.next.info if current_object.next else None}"
        )

        current_object = current_object.next


def main():
    first = create_objects(5)
    show_chain(first)


main()
