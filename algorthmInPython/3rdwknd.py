# #1111111111111111111111111111111111111111111111111111111111111111111111111111111
# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
 
# class LinkedQueue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
 
#     def is_empty(self):
#         if self.front==self.rear and self.front==None:
#             return True
#         return False
 
#     def put(self, data):
#         node=Node(data)
#         if LinkedQueue.is_empty(self):
#             self.front=self.rear=node
#         else:
#             self.rear.next=node
#             node.prev=self.rear
#             self.rear=node
 
#     def get(self):
#         if LinkedQueue.is_empty(self):
#             return None
#         tmp = self.front.data
#         self.front=self.front.next
#         if self.front==None:
#             self.rear=None
#         return tmp
 
#     def peek(self):
#         if LinkedQueue.is_empty(self):
#             return None
            
#         return self.front.data
        
 
# # Test code
# queue = LinkedQueue()
 
# print(queue.is_empty())
# for i in range(10):
#     queue.put(i)
# print(queue.is_empty())
 
# for _ in range(11):
#     print(queue.get(), end=' ')
# print()
 
# for i in range(20):
#     queue.put(i)
# print(queue.is_empty())
 
# for _ in range(5):
#     print(queue.peek(), end=' ')
# print()
 
# for _ in range(21):
#     print(queue.get(), end=' ')
# print()
# print(queue.is_empty())


# #222222222222222222222222222222222222222222222222222222222222222222222222222222222222

# class Stack:
#     def __init__(self):
#         self.list = list()
 
#     def push(self, data):
#         self.list.append(data)
 
#     def pop(self):
#         return self.list.pop()
 
# class Calculator:
#     def __init__(self):
#         self.stack = Stack()
 
#     def calculate(self, string):
#         elements=string.split()
#         for i in range(len(elements)):
#             Stack.push(self.stack , elements.pop())
#         total=int(self.stack.pop())
#         while len(self.stack.list):
#             num=int(self.stack.pop())
#             para=self.stack.pop()
#             if para=='+':
#                 total+=num
#             elif para=='-':
#                 total-=num
#             elif para=='*':
#                 total*=num
#             elif para=='/':
#                 total/=num
#             else:
#                 return "error (parameter)"
#         return total
 
# # Test code
# calc = Calculator()
# print(calc.calculate('4 6 * 2 / 2 +'))
# print(calc.calculate('2 5 + 3 * 6 - 5 *'))

# #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
 
# class Tree:
#     def __init__(self, root):
#         self.root = root
 
#     def preorder(self):
#         try:
#             if self==None:
#                 return
#             print(self.data)
#             Tree.preorder(self.left)
#             Tree.preorder(self.right)
#         except:
#             if self.root==None:
#                 return
#             print(self.root.data)
#             Tree.preorder(self.root.left)
#             Tree.preorder(self.root.right)

        
 
# # Test code
# root = Node(5, Node(2, Node(7, Node(4), Node(1)), Node(3)), Node(9, Node(6), Node(10)))
# tree = Tree(root)
# tree.preorder()

# #4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444



# def hash_func(key):
#     return ord(key[0]) % 10
 
# class HashTable:
#     def __init__(self):
#         self.table = [None]*10
 
#     def set(self, key, value):
#         self.table[hash_func(key)] = value
 
#     def get(self, key):
#         return self.table[hash_func(key)]
 
# class Node:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data
#         self.next = None
 
# class ChainedHashTable(HashTable):
#     def set(self, key, value):
#         index=hash_func(key)
#         if self.table[index]==None:
#             self.table[index]=Node(key,value)
#             return
#         node=self.table[index]
#         while True:
#             if node.key==key:
#                 node.data=value
#                 return
#             if node.next==None:
#                 node.next=Node(key,value)
#                 return
#             node=node.next

#     def get(self,key):
#         node=self.table[hash_func(key)]
#         while node!=None:
#             if node.key==key:
#                 return node.data
#             node=node.next
                
 
# # Test code

# ht = ChainedHashTable()
# ht.set('hello', 1)
# ht.set('hello2', 2)
# ht.set('hello3', 3)
# ht.set('hello4', 4)
 
# print(ht.get('hello'), end=' ')
# print(ht.get('hello2'), end=' ')
# print(ht.get('hello3'), end=' ')
# print(ht.get('hello4'), end=' ')
# print()
 
# ht.set('hello2', 5)
 
# print(ht.get('hello'), end=' ')
# print(ht.get('hello2'), end=' ')
# print(ht.get('hello3'), end=' ')
# print(ht.get('hello4'), end=' ')

import queue
a=queue.PriorityQueue()
a.put((10,'캠퍼스'))
a.put((1,'패스트'))
a.put((55,'완주반'))
a.put((11,'온라인'))

print(' '.join( [a.get()[1],a.get()[1],a.get()[1],a.get()[1]] ))