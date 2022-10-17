

vNum = []

num = int(input("Dime el 1º numero "))
vNum.append(num)
num = int(input("Dime el 2º numero "))
vNum.append(num)
num = int(input("Dime el 3º numero "))
vNum.append(num)

vNum.sort(reverse=True)
print(vNum)
print("El mayor es ", vNum[0])
ultimo = len(vNum)
print("El menor es ",vNum[ultimo-1])

print(max(vNum))
print(min(vNum))