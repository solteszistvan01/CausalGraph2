import time
from setsAndLogic import *
st = time.time()
V = {n : range(0,n) for n in range(32)}
et1 = time.time() #Time required for instantiating V in memory

Measurements = []

for i in range(32):
    Powerset(set(V[i]))
    Measurements.append(st-time.time())
    print("Elemszám:",len(V[i]),"; eltelt idő:", time.time() - st)

print(Measurements)