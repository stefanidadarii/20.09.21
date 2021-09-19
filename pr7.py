v=[2500,432,2345,4321,6754,8765,4332]
print('venitul saptamanal al întreprinderii =', sum(v))
print('media venitului zilnic =', sum(v)/7)
if v.index(max(v))==0: 
    print('ziua in care s-a obţinut cel mai mare venit este luni')
elif v.index(max(v))==1: 
    print('ziua in care s-a obţinut cel mai mare venit este marti')
elif v.index(max(v))==2: 
    print('ziua in care s-a obţinut cel mai mare venit este miercuri')
elif v.index(max(v))==3: 
    print('ziua in care s-a obţinut cel mai mare venit este joi')
elif v.index(max(v))==4: 
    print('ziua in care s-a obţinut cel mai mare venit este vineri')
elif v.index(max(v))==5: 
    print('ziua in care s-a obţinut cel mai mare venit este sambata')
else:
    print('ziua in care s-a obţinut cel mai mare venit este duminica')
if v.index(min(v))==0: 
    print('ziua cu venitul cel mai mic este luni')
elif v.index(min(v))==1: 
    print('ziua cu venitul cel mai mic este marti')
elif v.index(min(v))==2: 
    print('ziua cu venitul cel mai mic este miercuri')
elif v.index(min(v))==3: 
    print('ziua cu venitul cel mai mic este joi')
elif v.index(min(v))==4: 
    print('ziua cu venitul cel mai mic este vineri')
elif v.index(min(v))==5: 
    print('ziua cu venitul cel mai mic este sambata')
else:
    print('ziua cu venitul cel mai mic este duminica')