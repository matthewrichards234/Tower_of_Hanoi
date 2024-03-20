from node import Node

class Stack:
    def __init__(self, name, limit=10):
        self.top_item = None
        self.size = 0
        self.limit = limit
        self.name = name

    def has_space(self): 
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def push(self, value): # Add onto Stack.
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space.")

    def pop(self): # Remove from Stack.
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This stack is empty.")

    def peek(self): # Peek off the Stack.
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Nothing to see here!")

    def print_items(self):
        temp = self.top_item
        print_list = []
        while temp:
            print_list.append(temp.get_value())
            temp = temp.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))
