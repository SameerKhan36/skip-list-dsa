
# Group Members (Group no. 18)
# Sameer Ullah 19B-068-CS
# Muhammad Harris Hassan 19B-090-Cs

import random
class Node(object):
    def __init__(self, key, Level):
        self.key = key
        self.forward = [None] * (Level + 1)

class SkipList(object):
    def __init__(self, max_lvl, k):
# Highest level for this skip list
        self.MAX_LVL = max_lvl
        self.k = k

# creating header node and initialize key to -1
        self.header = self.create_Node(self.MAX_LVL, -1)

# Right now level of skip list
        self.level = 0
        self.lvl_list = []
        self.num_list = []

# creating new node
    def create_Node(self, lvl, key):
        n = Node(key, lvl)
        return n

# creating random level for node
    def randomLevel(self):
        lvl = 0
        while random.random() < self.k and lvl < self.MAX_LVL: lvl += 1
        return lvl

# inserting given key in skip list
    def insertElement(self, key):
        # creating and update array to initialize it
        current = self.header
        update = [None] * (self.MAX_LVL + 1)

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key: current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current == None or current.key != key:
            # Generating a random level skiplist  for node
            ranlevel = self.randomLevel()

            if ranlevel > self.level:
                for i in range(self.level + 1, ranlevel + 1):
                    update[i] = self.header
                self.level = ranlevel

            # create new node with random level generated
            n = self.create_Node(ranlevel, key)

            # inserting node by rearranging
            for i in range(ranlevel + 1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("You inserted key: {}".format(key))

    def deleteElement(self, search_key):
        # creating update array and initialize it
        current = self.header
        new = [None] * (self.MAX_LVL + 1)

        for i in range(self.level, -1, -1):
            while (current.forward[i] and
                   current.forward[i].key < search_key):
                current = current.forward[i]
            new[i] = current

        current = current.forward[0]

        if current != None and current.key == search_key:
            for i in range(self.level + 1):
                if new[i].forward[i] != current:
                    break
                new[i].forward[i] = current.forward[i]

# Remove levels having no elements
            while (self.level > 0 and
                   self.header.forward[self.level] == None):
                self.level -= 1
            print("{} deleted sucessfully".format(search_key))

    def searchElement(self, key):
        current = self.header
        for i in range(self.level, -1, -1):
            while (current.forward[i] and
                   current.forward[i].key < key):
                current = current.forward[i]

        current = current.forward[0]
        if current and current.key == key:
            print("You found: ", key)

    # Display of Skip list level wise
    def Show_List(self):
        print("Updated Skiplist")
        head = self.header
        for lvl in range(self.level + 1):
            self.lvl_list.append(f"Level {lvl}: ")
        node = head.forward[lvl]
        while (node != None):
            self.num_list.append(node.key)
            node = node.forward[lvl]
        index = 0
        if index < len(self.num_list):
            for i in self.num_list:
                print(self.lvl_list[index], i)
                index += 1

# driver code
def Driver():
    lst = SkipList(4,6)
    lst.insertElement(3)
    lst.insertElement(6)
    lst.insertElement(7)
    lst.insertElement(21)
    lst.insertElement(25)
    lst.Show_List()

# Searching for node 21
    lst.searchElement(21)

# Deleting node 21
    lst.deleteElement(21)

    lst.randomLevel()

Driver()
