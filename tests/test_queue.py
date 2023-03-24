"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import pytest
from src.queue import Queue, Node


@pytest.fixture
def queue_1():
    return Queue()


@pytest.fixture
def node_1():
    return Node("111", "222")


def test_queue_init(queue_1):
    """Проверка экземпляра 'queue' класса 'Queue' при инициализации"""
    assert queue_1.head is None
    assert queue_1.tail is None


def test_enqueue_queue(queue_1):
    """Функция проверки метода enqueue в классе Queue"""
    queue_1.enqueue('111')
    queue_1.enqueue('222')
    queue_1.enqueue('333')

    assert queue_1.head.data == '111'
    assert queue_1.head.next_node.data == '222'
    assert queue_1.tail.data == '333'
    assert queue_1.tail.next_node is None


def test_str_queue(queue_1):
    """Функция проверяет метод __str__ в классе Queue. """
    assert str(queue_1) == ""

    queue_1.enqueue("111")
    queue_1.enqueue("222")
    queue_1.enqueue("333")
    queue_1.enqueue("444")
    queue_1.enqueue("555")

    assert str(queue_1) == "111\n222\n333\n444\n555"


def test_init_node(node_1):
    assert node_1.data == "111"
    assert node_1.next_node == "222"


def test_dequeue_queue(queue_1):
    """Функция проверяет метод dequeue в классе Queue. """
    queue_1.enqueue("111")
    queue_1.enqueue("222")
    queue_1.enqueue("333")
    assert queue_1.dequeue() == '111'
    assert queue_1.dequeue() == '222'
    assert queue_1.dequeue() == '333'
    assert queue_1.dequeue() is None
