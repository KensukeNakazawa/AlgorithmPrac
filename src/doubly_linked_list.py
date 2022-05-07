from dataclasses import dataclass


class Node:
    def __init__(self, value: int):
        self.__value = value
        self.next_node: Node = None
        self.prev_node: Node = None

    @property
    def value(self):
        return self.__value


class DoublyLinkedList:

    def __init__(self):
        self.__head = None

    @property
    def head(self) -> Node:
        return self.__head

    @head.setter
    def head(self, node: Node):
        self.__head = node

    def insert(self, value: int):
        new_node = Node(value)
        current_node = self.head
        if current_node is None:
            current_node.next_node = new_node
            new_node.prev_node = new_node
            self.head = new_node
            return None

        while current_node != self.head:
            current_node = current_node.next_node
        current_node.prev_node.next_node = new_node
        new_node.prev_node = current_node.prev_node
        new_node.next_node = current_node
        current_node.prev_node = new_node

    def delete(self, value):
        current_node = self.head
        target_node = None
        while current_node != self.head:
            if current_node.value == value:
                target_node = current_node
            current_node = current_node.next_node
        target_node.prev_node.next_node = target_node.next_node
        target_node.next_node.prev_node = target_node.prev_node



# def main():
