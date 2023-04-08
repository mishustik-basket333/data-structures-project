class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


def data_verification(data):
    """Проверяет, являются ли данные словарём с ключом 'id', если да, то возвращает True, иначе сообщение"""
    if isinstance(data, dict) and "id" in data:
        return True
    else:
        print(f"Данные '{data}'не являются словарем или в словаре нет id")


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        # if data_verification(data):
        node = Node(data, self.head)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.head = node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        # if data_verification(data):
        node = Node(data)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
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

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке `LinkedList`"""
        node = self.head
        if node is None:
            return None

        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, id_name):
        """
            Возвращает первый найденный в `LinkedList` словарь с ключом 'id',
            значение которого равно переданному в метод значению.
            Если список пустой, то возвращает None
         """
        list_data = self.to_list()

        if list_data is None:
            return None

        for data in list_data:
            try:
                if data["id"] == id_name:
                    return data
            except TypeError:
                print('Данные не являются словарем или в словаре нет id')
