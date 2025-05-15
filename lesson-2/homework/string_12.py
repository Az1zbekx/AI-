n = input("Matn kiriting: ")
l = n.split()
x = ""
for i in l:
    x += "-" + i
x = x[1:]
print(x)