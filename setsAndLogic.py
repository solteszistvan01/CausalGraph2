from random import choice
import copy

class ExtendedInt: #Comparability with infty
    def __init__(self, param):
        self.param = param

    def __gt__(self, rhs):
        if type(self.param) == int:
            return self.param > rhs
        elif type(self.param) == str:
            #assuming correct inputs given str type
            return True
    def __lt__(self,rhs):
        if type(self.param) == int:
            return self.param < rhs #Raise error if input is not int or '$'!
        elif type(self.param) == str:
            return False

    def __add__(self,rhs):
        if type(self.param) == int:
            return self.param + rhs
        elif type(self.param) == str:
            return '$'

    def __repr__(self):
        return str(self.param)


def exists(D : set, P, Constants : list): #Feltételezett, hogy a konstansok a P predikátumfüggvény első paramétereibe lettek behelyettesítve és hogy a konstansok száma kisebb mindig, mint
    arguments = len(P.__code__.co_varnames)
    constants = len(Constants)
    if constants == arguments:
        return P(*Constants)
    List = []
    for x in D:
        C = copy.copy(Constants) #Deep copy solved the problem of the recursive call having NoneType parameter for the parameter of type list
        C.append(x)
        List.append(exists(D,P,C))
        for y in List:
            if y == True:
                return True
    return any(List)
#TODO: Return true as soon as a satisfying assignment exists!
#TODO: Make a function that returns all satisfying assignments!


def Powerset(V : set): #Prove, that this is indeed the Powerset of the input
    if V == set():
        return frozenset(set())
    results = {frozenset(V)}
    for x in V:
        results |= Powerset(V-{x})
    return results

def X(A : set, B: set):
    result = set()
    for x in A:
        for y in B:
            result |= {(x,y)}
    return result

def Choice(X): #For any object that is convertible to a list
    return choice(list(X))

def Min(storage):#Iterable object is assumed containing only ExtendedInts
    acc = Choice(storage)
    for x in storage:
        if acc > x:
            acc = x

    return acc