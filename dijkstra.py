from random import choice
from typing import *

from setsAndLogic import *

V = {1,2,3,4,5}
print("Alaphalmaz:", V)
VxV = X(V,V)
E = {(a,b) for (a,b) in VxV if a < b} #TODO : Sort the elements of E
print("Élhalmaz:",E)

G = (V,E)
s = Choice(V)
print("Tetszőleges s csúcs:",s)
w = {(a,b) : b-a for (a,b) in E}

t = dict() #minden v-re: s-ből v-be vezető legrövidebb út hossza
K = Choice({h for h in Powerset(V) if s in h and h != V})

print("Tetszőleges K részhalmaza az alaphalmaznak, melynek s eleme és mely nem azonos az alaphalmazzal:", K)

def EdgeTest(E : set, rhs, lhs):
    #Assuming, that E contains ordered pairs
    return (lhs,rhs) in E


print("V\\K:",V-K)

K_1 = {v for v in V if v not in K and exists(K,EdgeTest,[E,v])}
print("Azon V\\K-beli csúcsok, melyekbe vezet él K-beli csúcsból:",K_1)
tp = dict()
for v in K_1:
    tp.update({v : t[u] + w[(u,v)] for (u,v) in E if u in K})
print(tp)

#input : Domain : set, constants, variables, Predicate
#output :
