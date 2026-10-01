# тут нечего говорить, деревья....
class Node:
    def __init__(self, info: str):
        self.info = info
        self.right = None
        self.left = None


def show_tree(root: Node | None):
    if root is None:
        return

    current_objects = [root]

    while current_objects:
        new_objects = []

        for node in current_objects:
            print(node.info, end=" ")

            if node.left is not None:
                new_objects.append(node.left)

            if node.right is not None:
                new_objects.append(node.right)

        print()
        current_objects = new_objects


def create_tree(class_object: type, depth: int) -> list:
    first_object = Node("вершина")
    left_object = Node("левая вершина")
    right_object = Node("правая вершина")
    first_object.left = left_object
    first_object.right = right_object
    current_objects = [left_object, right_object]
    new_objects = []
    for _ in range(depth - 2):
        new_objects = []
        for node in current_objects:
            new_object_left = Node("левый ребенок")
            new_object_right = Node("правый ребенок")
            node.left = new_object_left
            node.right = new_object_right
            new_objects.extend([new_object_left, new_object_right])
        current_objects = new_objects

    return first_object


def main():
    root = create_tree(Node, 3)
    show_tree(root)


main()
