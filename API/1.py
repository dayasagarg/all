# no = ['ram','sham','god']
#
# for index, name in enumerate(no):
#     if index == 2:
#         print(name)



# for i in range(5):
#     print("1"+"2",end="")

from operator import add

aa = [1,2,3,4,5,6,7,8]
# b = [1,2,3,4]
# c = list(map(add,a,b))
# print(c)

# c = list(zip(a+b))
# c = [sum(i) for i in zip(a,b)]
# print(c)

# d = list(map(lambda x,y:x+y,a,b))
# print(d)

c = []



for i in aa:
    if 7 >= i >= 3:
        c.append(i)

print(c)