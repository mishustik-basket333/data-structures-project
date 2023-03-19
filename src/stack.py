class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        node = Node(data, self.top)
        self.top = node

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        node = self.top
        if not node:
            return None
        self.top = node.next_node
        return node.data

    def __str__(self):
        """Возвращает название класса"""
        return f"{self.__class__.__name__}"
#
#
# if __name__ == '__main__':
#     stack1 = Stack()
#     stack1.push("444")
#     print(str(stack1))
#     stack1.push("555")
#     print(str(stack1))
#     print(stack1)
