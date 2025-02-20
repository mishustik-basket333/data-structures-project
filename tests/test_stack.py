"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import pytest
from src.stack import Node, Stack


@pytest.fixture
def n1():
    return Node(100, None)


@pytest.fixture
def n2(n1):
    return Node(200, n1)


@pytest.fixture
def stack_1():
    return Stack()


def test_node_init(n1, n2):
    assert n2.data == 200
    assert n1.data == 100
    assert n2.next_node == n1
    assert n1.next_node is None


def test_stack_init(stack_1):
    assert stack_1.top is None


def test_stack_push(stack_1):
    stack_1.push(300)
    stack_1.push(400)

    assert stack_1.top.data == 400
    assert stack_1.top.next_node.data == 300


def test_stack_pop(stack_1):
    assert stack_1.pop() is None

    stack_1.push(300)
    stack_1.push(400)

    data = stack_1.pop()
    assert data == 400
    assert stack_1.top.data == 300


def test_str_stack(stack_1):
    """Тест для проверки __str__. Он должен возвращать строковое название класса Stack"""
    assert str(stack_1) == "Stack"
