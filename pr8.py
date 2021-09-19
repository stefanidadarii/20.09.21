t=[12,3,23,14,28,16,6,7,4,11,2,8,9,10,17,0,28,15,18,19,-3,-6,-1,0]
print('temperatura medie =', sum(t)/24)
print('maximul temperaturii =', max(t), ' minimul =', min(t))
for i in t:
    if i==max(t):
        print('ora (orele) la care s-a înregistrat temperatura maxima =', t.index(i)+1)
for i in t:
    if i==min(t):
        print('ora (orele) la care s-a înregistrat temperatura minima =', t.index(i)+1)
a=0
for i in t:
    if i<0:
        a=a+1
print('numarul de zile in care au fost inregistrate temperaturi mai jos de zero grade =', a)
b=0
for i in t:
    if i>sum(t)/24:
        b=b+1
print('numarul de zile in care au fost inregistrate temperaturi mai mari de media saptamanala =', b)