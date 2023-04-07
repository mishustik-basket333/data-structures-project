"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import pytest
from src.linked_list import LinkedList


@pytest.fixture
def ll_1():
    return LinkedList()


def test_init_linkedlist(ll_1):
    """Проверка экземпляра 'queue' класса 'Queue' при инициализации"""
    assert ll_1.head is None
    assert ll_1.tail is None


def test_insert_beginning_linkedlist(ll_1):
    ll_1.insert_beginning({'id': 4})
    assert ll_1.head.data == {'id': 4}
    assert ll_1.head.next_node == None
    assert ll_1.tail.data == {'id': 4}
    assert ll_1.tail.next_node is None

    ll_1.insert_beginning({'id': 3})
    assert ll_1.head.data == {'id': 3}
    assert ll_1.head.next_node.data == {'id': 4}

    ll_1.insert_beginning({'id': 2})
    ll_1.insert_beginning({'id': 1})
    assert ll_1.head.data == {'id': 1}
    assert ll_1.head.next_node.data == {'id': 2}
    assert ll_1.head.next_node.next_node.data == {'id': 3}
    assert ll_1.head.next_node.next_node.next_node.data == {'id': 4}
    assert ll_1.head.next_node.next_node.next_node.next_node is None


def test_insert_at_end_linkedlist(ll_1):
    ll_1.insert_at_end({'id': 5})
    assert ll_1.head.data == {'id': 5}
    assert ll_1.head.next_node is None
    assert ll_1.tail.data == {'id': 5}
    assert ll_1.tail.next_node is None

    ll_1.insert_at_end({'id': 6})
    assert ll_1.tail.data == {'id': 6}
    assert ll_1.tail.next_node is None


def test_str_linkedlist(ll_1):
    assert str(ll_1) == "None"
    ll_1.insert_beginning({'id': 3})
    ll_1.insert_beginning({'id': 2})
    assert str(ll_1) == "{'id': 2} -> {'id': 3} -> None"


def test_data_verifiction(ll_1):
    assert ll_1.insert_beginning([1, 2, 3, 4, 5]) is None
    assert ll_1.insert_beginning({'name': 1, 'username': 'lazzy508509'}) is None

    assert ll_1.insert_at_end([1, 2, 3, 4, 5]) is None
    assert ll_1.insert_at_end({'name': 1, 'username': 'lazzy508509'}) is None

def test_get_data_by_id(ll_1):
    assert ll_1.get_data_by_id(3) == None

    ll_1.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll_1.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll_1.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll_1.insert_beginning({'id': 0, 'username': 'serebro'})

    assert ll_1.get_data_by_id(0) == {'id': 0, 'username': 'serebro'}
    assert ll_1.get_data_by_id(3) == {'id': 3, 'username': 'mosh_s'}
