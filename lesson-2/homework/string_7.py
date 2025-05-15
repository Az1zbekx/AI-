n = input("Matn kiriting: ")
l = n.split()
a = input("Qaysi so'zni o'zgartirishni hohlaysiz: ")
b = input("Qanday so'zga o'zgarsin: ")
k = l.index(a)
l[k] = b
print(*l)
