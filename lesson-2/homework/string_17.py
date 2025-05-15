n = input("Matn kiriting: ")
m = "aeuioAEUIO"
for i in n:
    if i in m:
        n = n.replace(i, "*")
print(n)