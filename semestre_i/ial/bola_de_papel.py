#!/usr/bin/env python

import sys
out = sys.stdout.write


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_linked_list(node, stop_data):
    if (node.data is not stop_data):
        out(str(node) + ' -> ')
        print_linked_list(node.next, stop_data)
    else:
        out(str(node) + ' -> nil\n')


def setup_circle(number_of_students, initial_student):
    first_student = Node(0, None)
    head = first_student if initial_student == 0 else None
    previous = first_student
    for i in range(1, number_of_students):
        next = Node(i, None)
        previous.next = next
        previous = next
        if (initial_student == i):
            head = previous

    previous.next = first_student
    return head


def play()


def main():
    head = setup_circle(8, 4)
    print_linked_list(head, head.data-1)
    folhas = 1
    bola = folhas * 2



if __name__ == "__main__":
    main()
