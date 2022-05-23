import numpy as np

n = input("number of data: ")
dim = input("dimension of data: ")
datas = list()

for i in range(int(n)):
    data = list()
    print("data "+str(i+1)+" is: ")
    for j in range(int(dim)):
        number = int(input())
        data.append(number)
    datas.append(data)

avg = list()
for j in range(int(dim)):
    sum = 0
    for i in range(int(n)):
        sum += datas[i][j]
    sum /= int(n)
    avg.append(sum)

for i in range(int(n)):
    for j in range(int(dim)):
        datas[i][j] -= avg[j]
datas = np.array(datas)

U, Sigma, Vh = np.linalg.svd(datas)
num = 1
for col in Vh:
    print(str(num)+" component is:")
    print(col)
    num += 1

print("regression line: c*",end="")
print(Vh[0],end="")
print(" + ",end="")
print(avg)