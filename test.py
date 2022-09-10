a={"A":0,"B":2,"C":4}
b = {"A":2,"B":3,"C":-4}
for key in a.keys():
    a[key] += b[key]
print(a)