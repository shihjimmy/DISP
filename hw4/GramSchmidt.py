""" 
    Use the Gram-Schmidt method to convert  1, n, n^2, n^3, n^4 into an orthonormal 
    vector set where n = [0, 10]
"""
a = list()
a0 = [1,1,1,1,1,1,1,1,1,1,1]
a1 = [0,1,2,3,4,5,6,7,8,9,10]
a.append(a0)
a.append(a1)

for i in range(2,5):
    temp = list()
    for j in range(11):
        temp.append(a1[j]**i)
    a.append(temp)

length = 11
def innerProduct(a,b):
    res = 0
    for i in range(length):
        res += a[i]*b[i]
    return res

def normalize(a):
    res = innerProduct(a,a)**0.5
    for i in range(length):
        a[i] = a[i]/res
    return a

def GramSchmidt(set_of_vectors):
    set_of_vectors[0] = normalize(set_of_vectors[0])
    for i in range(1,len(set_of_vectors)):
        total = [0,0,0,0,0,0,0,0,0,0,0]
        for j in range(i):
            multiple = innerProduct(set_of_vectors[i],set_of_vectors[j])
            temp = [x*multiple for x in set_of_vectors[j]]
            for k in range(length):
                total[k] += temp[k]
        for t in range(length):
            set_of_vectors[i][t] -= total[t]
        set_of_vectors[i] = normalize(set_of_vectors[i])
    return set_of_vectors

GramSchmidt(a)
for i in range(len(a)):
   print(a[i])