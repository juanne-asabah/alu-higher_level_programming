#!/usr/bin/python3
"""This module defines classes for a singly linked list implementation.

It provides a Node class that performs data validation and a SinglyLinkedList
class that keeps its nodes sorted in increasing order upon insertion.
"""


class Node:
    """A class that defines a node of a singly linked list.

    This class encapsulates data and a reference to the next node, ensuring
    strict type safety for integer values and node linkages.
    """

    def __init__(self, data, next_node=None):
        """Initialise a new Node instance with data and an optional next link.

        Args:
            data (int): The integer value stored inside the node.
            next_node (Node, optional): The next node link. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in the node.

        Returns:
            int: The node data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with strict type validation.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next connected node instance.

        Returns:
            Node: The subsequent node linked in the list, or None.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node link with validation.

        Args:
            value (Node): The next node object or None.

        Raises:
            TypeError: If value is not None and not a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list structure.

    This class maintains an internal head node reference and handles sorting,
    iteration, and visual presentation requirements.
    """

    def __init__(self):
        """Initialise an empty SinglyLinkedList instance."""
        self.__head = None

    def __str__(self):
        """Generate a string representation of the linked list for printing.

        Each node data value is separated by a new line format.

        Returns:
            str: The structural textual breakdown of the collection.
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node into the list in ascending sorted order.

        Args:
            value (int): The numerical value to insert into the sequence.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
