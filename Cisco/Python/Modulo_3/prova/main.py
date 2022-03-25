t = [[3-i for i in range(3)] for j in range (3) ]
s = 0
for i in range (3):
    s += t[i][i]
print(s)

#==============================

x = 1
x = x == x
print(x)


# ==============================
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

# ==============================
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c +d + e)

# ==============================

my_list = [3,1,-2]
print(my_list[my_list[-1]])

# ==============================

for i in range(1):
    print("#")
else:
    print("#")


# ==============================

# my_list = [[0,1,2,3] for i in range (2)]
# print(my_list[2][0])

# ==============================

my_list = [i for i in range(-1,2)]
print(my_list)

# ==============================

vals = [0,1,2]
vals.insert(0,1)  # isso é um append
print("dps do insert: ", vals)
del vals[1] # vals = [0,2]
print(vals)

# ===========================
vals = [0,1,2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

# ===========================

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

# ==================================
my_list = [1,2,3,4]
print(my_list[-3:-2])

# =========================
nums = [1,2,3]
vals = nums
del vals[1:2]
print(nums, vals)

# =========================
nums = [1,2,3]
vals = nums[-1:-2]
print(nums, vals)

# =========================

my_list_1 = [1,2,3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0,v)
print(my_list_2 ) 

# =========================
my_list = [1,2,3]
for v in range (len(my_list)):
    my_list.insert(1,my_list[v])
print(my_list)

# =========================
var = 1
while var < 10:
    print("#")
    var = var << 1