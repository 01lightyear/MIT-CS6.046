import random

class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        # forward is a list of pointers to next nodes in each level
        self.forward = [None] * (level + 1)

class SkipList:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        # Create header node and initialize level
        self.header = SkipListNode(-1, self.MAX_LEVEL)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        # Start from the highest level of the skip list
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Move to level 0
        current = current.forward[0]

        # If current is None or key is not present, insert it
        if current is None or current.key != key:
            lvl = self.random_level()

            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = SkipListNode(key, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return True
        return False

    def delete(self, key):
        update = [None] * (self.MAX_LEVEL + 1)
        current = self.header

        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Remove levels which have no elements
            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display_list(self):
        print("Skip List:")
        for i in range(self.level + 1):
            current = self.header.forward[i]
            print("Level {}: ".format(i), end="")
            while current:
                print(current.key, end=" ")
                current = current.forward[i]
            print("")
def main():
    skip_list = SkipList()
    elements = [3, 6, 7, 9, 12, 19, 17, 26, 21, 25]

    # 插入元素
    for elem in elements:
        skip_list.insert(elem)
    print("插入元素后的跳表:")
    skip_list.display_list()

    # 搜索元素
    search_keys = [19, 15]
    for key in search_keys:
        found = skip_list.search(key)
        print(f"搜索元素 {key} {'存在' if found else '不存在'}于跳表中。")

    # 删除元素
    skip_list.delete(19)
    print("删除元素19后的跳表:")
    skip_list.display_list()

    # 搜索元素19
    found = skip_list.search(19)
    print(f"删除后的搜索元素19 {'存在' if found else '不存在'}于跳表中。")

if __name__ == "__main__":
    main()