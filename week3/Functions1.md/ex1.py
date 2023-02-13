def Ounces(weight):
    weight2 = weight / 28.3495
    return weight2

a = int(input())
a = Ounces(a)
print(f"{a} ounces")