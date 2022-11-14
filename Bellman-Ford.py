
from setsAndLogic import *

V = {1,2,3,4,5,6,7,8,9,10}
E = {(a,b) for (a,b) in X(V,V) if a < b}
G = (V, E)
s = Choice(V)
v = Choice(V-{s}) #Legalább két eleme van V-nek
w = {(a,b) : b-a for (a,b) in E}

print("V:",V,"\n","E:",E,"\n","s:",s,"\n","v:",v,"\n","w:",w)

#t0 függvények

t0 = {v : ExtendedInt('$') for v in G[0]}
t1 = {(u,v) : w[u,v] for (u,v) in G[1]}
t2 = {(u,v) : min({t1[u] + w[(u,v)] for (u,v) in G[1]}) for (u,v) in G[1]}
print(t2)

