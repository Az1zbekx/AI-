n = input("Birinchi matnni kiriting: ")
m = input("Ikkinchi matnni kiriting: ")
if n in m:
    print(f"{m} matnining ichida {n} mavjud")
elif m in n:
    print(f"{n} matnining ichida {m} mavjud")
else:
    print("Hech bir matn ichida boshqasi mavjud emas")
