from interface import Interface
from toolbox import *


class Assembly(Interface):
    def __init__(self):
        self._assembly = []

    def __len__(self):
        return len(self._assembly)

    def calculateCentreOfMass(self):
        total = 0.0
        for sh in self._assembly:
            total += sh.calculateCentreOfMass()
        return total

    def add(self, sh):
        self._assembly.append(sh)

    def remove(self, sh):
        self._assembly.remove(sh)

    def makeobjects(self, key):
        from blade import Blade
        from engine import Engine
        from rotor import Rotor
        from stator import Stator
        from turbine import Turbine
        low_key = str.lower(key)
        dispatch_dict = SpecialDic()
        dispatch_dict["blade"] = Blade
        dispatch_dict["stator"] = Stator
        dispatch_dict["rotor"] = Rotor
        dispatch_dict["turbine"] = Turbine
        dispatch_dict["engine"] = Engine
        return dispatch_dict[low_key]

    def retobjectlist(self, subAssy, globalDict):
        listofobjects = []
        for part in subAssy:
            for key, val in part.items():
                for i in range(val):
                    extra = self.makeobjects(key)
                    listofobjects.append(extra(globalDict))
        return listofobjects

    def getChildElement(self, globalDict):
        tempList = self.retobjectlist(globalDict[self._partName], globalDict)
        for part in tempList:
            self.add(part)

    def clear(self):
        print("Clearing all parts from Assembly")
        self._assembly = []