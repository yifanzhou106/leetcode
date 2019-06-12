class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hashlist = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        if not self.hashlist[index]:
            singlenode = Node(key, value)
            self.hashlist[index] = singlenode
        else:
            singlenode = self.hashlist[index]
            while singlenode.next:
                if key == singlenode.key:
                    singlenode.val = value
                    return
                singlenode = singlenode.next
            if key == singlenode.key:
                singlenode.val = value
                return
            singlenode.next = Node(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.size
        if not self.hashlist[index]:
            return -1
        else:
            singlenode = self.hashlist[index]
            while singlenode.next:
                if key == singlenode.key:
                    return singlenode.val
                singlenode = singlenode.next
            if key == singlenode.key:
                return singlenode.val
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.size
        if self.hashlist[index]:
            singlenode = self.hashlist[index]
            prenode = singlenode
            if key == singlenode.key:
                self.hashlist[index] = singlenode.next
                return
            singlenode = singlenode.next
            while singlenode:
                if key == singlenode.key:
                    prenode.next = singlenode.next
                    return
                prenode = singlenode
                singlenode = singlenode.next



                # Your MyHashMap object will be instantiated and called as such:
                # obj = MyHashMap()
                # obj.put(key,value)
                # param_2 = obj.get(key)
                # obj.remove(key)