n = input("Matn kiriting: ")
x = "0123456789"
for i in n:
    if i in x:
        print("Siz kiritgan matnda raqam mavjud")
        exit()
print("Siz kiritgan matnda raqam mavjud emas")
