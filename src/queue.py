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
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass

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
#
#
# if __name__ == '__main__':
#     queue = Queue()
#     queue.enqueue('data1')
#     queue.enqueue('data2')
#     queue.enqueue('data3')
#
#     print(queue.head.data)
#     print(queue.head.next_node.data)
#     print(queue.tail.data)
