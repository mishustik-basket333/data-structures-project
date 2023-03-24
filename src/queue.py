class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        object_data = self.head
        if not object_data:
            return None
        else:
            self.head = object_data.next_node
            return object_data.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ""
        head = self.head
        result = []
        while head:
            result.append(head.data)
            head = head.next_node
        return "\n".join(result)


# if __name__ == '__main__':
#     queue = Queue()
#     queue.enqueue('data1')
#     queue.enqueue('data2')
#     queue.enqueue('data3')
#     queue.enqueue('data4')
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
