import random

hash_table = [[] for _ in range(10)]
hash_table[0].append((10,'a'))
hash_table[0].append((7,'c'))

print(hash_table)
del hash_table[0][1]

for k, v in hash_table[0]:
    print(k, v)
class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    """
    해시 테이블(Hash Table)을 나타내는 클래스.

    :param capacity: 해시 테이블의 초기 버킷(bucket) 개수(혹은 내부 배열 크기)
    :type capacity: int
    """

    def __init__(self, capacity: int):
        """
        HashTable 인스턴스를 초기화합니다.

        :param capacity: 초기 해시 테이블 배열(버킷) 크기
        :type capacity: int
        """
        self.__capacity = capacity
        self.__buckets = [[] for _ in range(capacity)]

    def insert(self, key: object, value: object) -> None:
        """
        해시 테이블에 (key, value) 쌍을 삽입합니다.
        만약 key가 이미 존재한다면, 해당 key에 대한 value를 갱신합니다.

        :param key: 해시 테이블에 저장할 키(key)
        :type key: object
        :param value: key와 매핑할 값(value)
        :type value: object
        :return: None
        :rtype: None
        """
        #bucket 번호 계산.
        bucket_num = hash(key)%self.__capacity
        for entry in self.__buckets[bucket_num]:
            if entry.key == key:
                entry.value = value
                return
        self.__buckets[bucket_num].append(KeyValuePair(key, value))



    def find(self, key: object) -> object:
        """
        주어진 key에 해당하는 value를 해시 테이블에서 탐색해서 반환합니다.

        - 해당 key를 찾지 못하면 None을 반환합니다.
        - 찾으면 해당 value를 반환합니다.

        :param key: 탐색할 키
        :type key: object
        :return: key에 매핑된 value (없으면 None)
        :rtype: object
        """
        bucket_num = hash(key)%self.__capacity
        for entry in self.__buckets[bucket_num]:
            if entry.key == key:
                return entry.value
        return None

    def remove(self, key: object) -> object:
        """
        주어진 key를 해시 테이블에서 제거합니다.

        - 해당 key가 존재하지 않으면 None을 반환합니다.
        - 존재한다면, 제거 후 원래 매핑된 value를 반환합니다.

        :param key: 제거할 키
        :type key: object
        :return: 제거된 key에 매핑된 value (없으면 None)
        :rtype: object
        """
        bucket_num = hash(key) % self.__capacity
        for i, entry in enumerate(self.__buckets[bucket_num]):
            if entry.key == key:
                value = entry.value
                del self.__buckets[bucket_num][i]
                return value
        return None


# class Node(object):
#     def __init__(self, data: object) -> None:
#         self.data = data
#         self.next = None
# class LinkedList(object):
#     def __init__(self):
#         self.head = None
#
#     def append(self, data: object) -> None:
#         new_node = Node(data)
#         current = self.head
#         if self.head is None:
#             self.head = new_node
#         else:
#             # current가 list의 맨 마지막 원소를 가르키게 한다
#             while current.next is not None:
#                 current = current.next
#             current.next = new_node
#     def __iter__(self):
#         self.current = self.head
#         return self
#     def __next__(self):
#         if self.current is not None :
#             data = self.current.data
#             self.current = self.current.next
#             return data
#         else :
#             raise StopIteration
#
#     def remove(self, data: object) -> None:
#         # list에서 data가 있는지 확인하고 있으면 지우고 data를 return 한다. 없으면 None return.
#         prev = None
#
#         current = self.head
#         while current is not None:
#             if current.data == data:
#                 prev.next = current.next
#                 return data
#             else:
#                 prev = current
#                 current = current.next
#
#         return None
#
#
#     def __repr__(self):
#         current = self.head
#         str = ''
#         while current is not None:
#             str += current.data + '->'
#             current = current.next
#         return str
# L = LinkedList()
# L.append('a')
# L.append('b')
# L.append('c')
# print(L)
# L.remove('b')
# print(L)

# h = HashTable(100)
# for _ in range(100) :
#     key = random.randint(0, 100)
#     value = random.randint(0, 100)
#     h.insert(key, value)
# for _ in range(100):
#     k = random.randint(0, 100)
#     # if k in the hash table, remove it
#     if h.find(k) :
#         h.remove(k)
#         print(f"key = {k}, value = {value} is deleted.")
#     else :
#         print("Key not found")

# h = HashTable(100)  # HashTable 객체 생성.
#
#
# d = {}
# random.seed(90)
# print("test")
# # #100개의 key, value를 랜덤하게 생성하여 hash_table에 삽입.
# for i in range(100):
#     key = random.randint(0,100)
#     value = random.randint(0,100)
#     print(key, value)
#     h.insert(key, value)
#     d[key] = value
#
# print(d)
# #100개의 k를 랜덤으로 생성 후 key가 hash table에 있으면 지우고, 제거되었음을 출력으로 알리기. 존재하지 않는 경우 발견되지 않았다고 출력으로 알리기.
# for i in range(100):
#     key = random.randint(0, 100)
#     print(key)
#     dic_val = d.get(key, None)
#     value = h.find(key)
#     if dic_val != value:
#         print(dic_val, value)
#     if value:
#         h.remove(key)
#         del d[key]
#         print(f"key = :{key}, value = :{value} is found and deleted.")
#     else:
#          print(f"key = {key} not found")
#  #내부 메서드를 구현하기 전에 이를 사용하는 코드는 작성할 수 있음.
#




class Node(object):
    def __init__(self, data: object) -> None:
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        
    def remove(self, data):
        prev = None
        current = self.head
        while current is not None:
            if current.data == data:   #현 노드에서 내가 원하는 데이터와 일치하면
                prev.next = current.next
                return data
            else:  #다음 노드로 넘어가기?
                prev = current
                current = current.next
        return None
        
    def __repr__(self):
        str = ''
        current = self.head
    
        while current is not None:
            str += current.data + '->'
            current = current.next
        return str
    def __iter__(self):
        self.current = self.head
        return self
    def __next__(self):
        if self.current is not None:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration
L = LinkedList()
L.append('a')
L.append('b')
L.append('c')
for data in L:
    print(data)
print(L)
L.remove('b')
print(L)





