# #111111111111111111111111111111111111111111111111111111
# with open('./a.csv','r') as f:
#     total=0
#     content=f.read()
#     nums=content.split(",")
#     for i in nums:
#         total+=int(i)
#     print(total)


# #22222222222222222222222222222222222222222222222222222222
# class Median:
#     def __init__(self):
#         self.nums=[]
 
#     def get_item(self, item):
#         self.nums.append(item)
 
#     def clear(self):
#         self.nums.clear()
 
#     def show_result(self):
#         self.nums.sort()
#         siz=len(self.nums)
#         if siz % 2:
#             print(self.nums[siz//2])
#         else:
#             print((self.nums[siz//2-1]+self.nums[siz//2])/2)
            

 
# median= Median()
# for x in range(10):
#     median.get_item(x)
# median.show_result()
 
# median.clear()
# for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
#     median.get_item(x)
# median.show_result()

# #3333333333333333333333333333333333333333333333333333333333333333

# class Animal:
#     def __init__(self, name):
#         self.name = name
 
#     def speak(self):
#         print(self.name + ' cannot speak.')
 
#     def move(self):
#         print(self.name + ' cannot move.')
 
 
# class Dog(Animal):
#     def move(self):
#         print(self.name,"moves like a jagger.")
 
 
# class Retriever(Dog):
#     def speak(self):
#         print(self.name, "is smart enough to speak.")
 
 
# dog = Dog('Nancy')
# dog.speak()
# dog.move()
 
# super_dog = Retriever('Michael')
# super_dog.speak()
# super_dog.move()


#4444444444444444444444444444444444444444444444444444444444444444444


# class Foo:
#     bar="A"

#     def __init__(self):
#         self.bar="B"

#     class Bar:
#         bar="C"

#         def __init__(self):
#             self.bar="D"
    
# a=Foo()
# print(a.bar)
# print(Foo.bar)  # A 출력
# print(Foo().bar)  # B 출력
# print(Foo.Bar.bar)   # C 출력
# print(Foo.Bar().bar) # D 출력



import datetime
now =datetime.datetime.date

print(now)
print(now1)