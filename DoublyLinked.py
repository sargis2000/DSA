from abc import ABC, abstractmethod
from typing import Any


class ELEMENT:
    """It's a doubly linked list node"""

    def __init__(self, data: Any):
        self.data: Any = data
        self.next: None | ELEMENT = None
        self.prev: None | ELEMENT = None

    def __str__(self) -> str:
        return str(self.data)


class AbstractDoublyLinkedList(ABC):
    """An abstract class that defines the interface for a doubly linked list."""

    @abstractmethod
    def push_front(self, value: Any) -> None:
        pass

    @abstractmethod
    def push_back(self, value: Any) -> None:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def front(self) -> ELEMENT | None:
        pass

    @abstractmethod
    def back(self) -> ELEMENT | None:
        pass

    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def emplace(self, value: Any, index: int) -> None:
        pass

    @abstractmethod
    def insert(self, value, index=False) -> None:
        pass


class DoublyLinkedList(AbstractDoublyLinkedList):
    """The DoublyLinkedList class is a class that creates a doubly linked list"""

    def __init__(self) -> None:
        self.head: None | ELEMENT = None
        self.first: bool = False
        self.reverse: bool = False

    def push_front(self, value: Any) -> None:
        """
        We create a new element, set its next to the current head, set the current head's previous to the new element, and
        then set the list's head to the new element

        :param value: The value to be added to the list
        """
        new_value = ELEMENT(value)
        new_value.next = self.head
        if self.head is not None:
            self.head.prev = new_value
        self.head = new_value

    def push_back(self, value: Any) -> None:
        """
        We create a new element, and if the list is empty, we set the head to the new element. Otherwise, we find the last
        element in the list, and set its next value to the new element

        :param value: Any
        :type value: Any
        :return: None
        """
        new_value = ELEMENT(value)
        if self.head is None:
            self.head = new_value
            return None
        last_value = self.head
        while last_value.next is not None:
            last_value = last_value.next
        else:
            last_value.next = new_value
            new_value.prev = last_value

    def size(self) -> int:
        """
        It returns the length of the list.
        :return: The size of the list.
        """
        return self.__len__()

    def front(self) -> ELEMENT | None:
        """
        If the head is None, return None. Otherwise, while the head's previous node is not None, set the head to the head's
        previous node. Then, return the head
        :return: The head of the list.
        """
        if self.head is None:
            return None
        while self.head.prev is not None:
            self.head = self.head.prev
        return self.head

    def back(self) -> ELEMENT | None:
        """
        It returns the last element of the linked list.
        :return: The last node in the linked list.
        """
        if self.head is None:
            return None
        while self.head.next is not None:
            self.head = self.head.next
        return self.head

    def begin(self):
        """
        It returns an iterator object
        :return: The iterator object itself.
        """
        return self.__iter__()

    def end(self):
        """
        It returns the reversed string.
        :return: The reversed iterator.
        """
        return self.__reversed__()

    def empty(self):
        """
        If the head node has a data attribute, then the list is not empty
        :return: a boolean value.
        """
        return hasattr(self.head, "data")

    def emplace(self, value: Any, index: int) -> None:
        """
        If the list is empty, push the value to the front. Otherwise, iterate through the list until the index is reached,
        then insert the value

        :param value: the value to be inserted
        :param index: the index where the new element should be placed
        """
        if self.head is None:
            self.push_front(value)
        else:
            self.head = self.front()
            count = 0
            while count != index:
                try:
                    # print(self.head)
                    self.head = self.head.next
                    count += 1
                except AttributeError:
                    self.push_back(value)
                    break

            else:
                new = ELEMENT(value)
                new.prev = self.head.prev
                new.next = self.head
                self.head.prev.next = new
                self.head.prev = new

    def insert(self, value, index=False):
        """
        If the index is not false, then insert the value at the index, otherwise insert the value at the front of the list

        :param value: The value to insert into the list
        :param index: The index to insert the value at, defaults to False (optional)
        """
        if index:
            self.emplace(value, index)
        else:
            self.push_front(value)

    def __delete__(self, key: Any) -> None:
        """
        If the key is in the list, delete it

        :param key: The key to be deleted
        :return: The value of the key.
        """

        if self.head is None:
            print("Deletion Error: The list is empty.")
            return

        if self.head == key:
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

        if current is None:
            print("Deletion Error: Key not found.")
        else:
            previous.next = current.next

    def splice(self, other) -> None:
        """
        It takes the last node of the first list and connects it to the first node of the second list.

        :param other: The DoublyLinkedList that you are splicing into the end of the current DoublyLinkedList
        """
        if not isinstance(other, DoublyLinkedList):
            raise TypeError("Cant splice")
        else:
            last = self.back()
            last.next = other.front()
            other.front().prev = last

    def clear(self):
        """
        It clears the list.
        """
        self.head = self.front()
        while self.head is not None:
            self.__delete__(self.head)

    def __len__(self):
        """
        For each element in self, increment count by 1 and return count.
        :return: The number of items in the list.
        """
        count = 0
        for _ in self:
            count += 1
        return count

    def __reversed__(self):
        """
        __reversed__() is a function that returns the reversed version of the list
        :return: The object itself.
        """
        self.reverse = True
        return self

    def __iter__(self):
        """
        The function iterates through the list, starting at the front if the list is not reversed, and at the back if it is
        reversed
        :return: The iterator object itself.
        """
        self.head = self.back() if self.reverse else self.front()
        self.first = True
        return self

    def __next__(self):
        """
        If the list is empty, raise a StopIteration exception. If the list is not empty, return the head of the list. If the
        list is not empty and the first flag is set, return the head of the list and unset the first flag. If the list is
        not empty and the reverse flag is set, return the previous node of the head of the list. If the list is not empty
        and the reverse flag is not set, return the next node of the head of the list
        :return: The next node in the list.
        """
        if self.head is None:
            raise StopIteration
        if self.first:
            self.first = False
            return self.head
        if self.reverse:
            if self.head.prev is None:
                self.reverse = False
                raise StopIteration
            self.head = self.head.prev
            return self.head
        else:
            if self.head.next is None:
                raise StopIteration
            self.head = self.head.next
            return self.head

    def __str__(self):
        """
        The function takes a linked list and returns a string representation of the linked list
        :return: The string representation of the linked list.
        """
        result = f"linkedlist["
        for i in self:
            result += i.__str__() + ", "
        return result + "]"


if __name__ == "__main__":
    dllist = DoublyLinkedList()
    dllist.push_back(7)
    dllist.push_front(12)
    dllist.push_back(8)
    dllist.push_front("sdfds")
    dllist.push_front(62)
    dllist.emplace(777, 3)
