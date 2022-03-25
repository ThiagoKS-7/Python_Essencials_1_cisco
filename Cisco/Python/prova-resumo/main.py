# i = 0
# while i < i + 2:
#     i += 1
#     print("*") 
# else:
#      print("*") 
# ==================
lst = [[x for x in range(3)] for i in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
# ==================
my_list = [x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
# ==================
dct= {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1], end="")
# ==================
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print('\n\naqui: ', fun(0,3))
# ==================
# dd = {"1": "0", "0": "1"}
# for x in dd.vals():
#     print(x, end="")
# ==================
print(1//2)
# ==================
def fun(x):
    if x % 2 == 0:
        return 1
    else: 
        return 2
print(fun(fun(2)))
# ==================
my_list = [1,2]

for v in range(2):
    my_list.insert(-1, my_list[v])
print(my_list)
# ==================
z = 0
y = 10
x = y < z and z > y or y > z and z < y
print(x)
# ==================
x = 1//5 + 1/5
print(x)
# ==================
print("a","b","c",sep="sep")
# ==================
# def func(a,b):
#     return b ** a

# print(func(b=2, 2))
# ==================
a =1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)
# ==================
tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
# ==================
# my_tup = (1,2)
# my_tup[1] = my_tup[1] + my_tup[0] # WAIT, THATS ILLEGAL
# print(my_tup)
# ==================
nums = [1,2,3]
vals = nums
print(vals,nums)
# ==================
lst = [i for i in range(-1,-2)]
print(len(lst))
# ==================
x = 1
y = 2
x, y, z = x, x ,y
z, y, z = x, y ,z
print(x,y,z)
# ==================
nums = [1,2,3]
vals = nums
del vals[:]
print('aqui:', vals,nums)
# ==================
x = 3
y = 2
x = x % y
x = x % y
y = y % x
print(y)
# ==================
# def function1(a):
#     return None

# def function2(a):
#     return function1(a) * function1(a)

# print(function2(2))
# ==================
x = 2.0
y = 4.0
print(y ** (1/x))
# ==================
# ==================
# ==================
# ==================
# ==================
# ==================