class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data, self.head)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        # elif not self.tail:
        #     self.tail = self.head
        #     self.head = node
        else:
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        # elif not self.tail:
        #     self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            if ll_string == '':
                ll_string += f'{str(node.data)} ->'
            else:
                ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string


ll = LinkedList()
#
# # # Добавляем данные
ll.insert_beginning({'id': 1})
# # ll.insert_at_end({'id': 2})
# # ll.insert_at_end({'id': 3})
# # ll.insert_beginning({'id': 0})
#
# # # Добавляем данные
# ll.insert_beginning({'id': 1})
# ll.insert_beginning({'id': 0})
# ll.insert_beginning({'id': -1})
# ll.insert_at_end({'id': 2})
# ll.insert_at_end({'id': 3})
# ll.insert_beginning({'id': -2})
# ll.insert_at_end({'id': 4})
# ll.insert_at_end({'id': 5})
# ll.insert_beginning({'id': -3})
# ll.insert_at_end({'id': 6})
#
# # # Печатаем данные
print(ll)
print(str(ll))
# print("{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")
# assert str(ll) == "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None"
