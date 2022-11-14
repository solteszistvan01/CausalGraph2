import sys
from pathlib import PurePosixPath
from dijkstra import *

class Event:
    def __init__(self, name : str):
        self.__name = name

    def getName(self):
        return self.__name

    def __repr__(self):
        return f"{repr(self.__name)}"

class CausalGraph:
    class Path:
        def __init
        pass
    def __init__(self, events : set, causalities: set):
        self.__events = events
        self.__causalities = causalities

    def getEvents(self):
        return self.__events
    def getCausalities(self):
        return self.__causalities


    def Paths(self,event : Event, events : set ,distance : int):
        def __init__(self, *args):


        return results
        pass

def PathsFrom(events : set, event : Event, distance : int):
    pass

def writeTo(file, data: set):
    pass


def main(argv):
    Event = Event(sys.argv[0])
    Graph = CausalGraph(PurePosixPath(sys.argv[1]))
    Distance = (int(argv[2]))

    S = FurthestEvents(Event, Graph, Distance)
    P = PathsFrom(S, Event, Graph)


    File = open("result.txt","w")
    writeTo(File, S)
    writeTo(File, P)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
