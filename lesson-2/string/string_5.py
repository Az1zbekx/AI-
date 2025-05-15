n = input("Matn kiriting: ")
a = "aeiouAEIOU"
x, y = 0, 0
for i in n:
    if i in a:
        x += 1
    else:
        y += 1
print(f"Matnda {x} ta unli va {y} ta undosh harf bor")
