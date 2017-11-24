from assembly import Assembly


class Stator:
    def __init__(self, globalDict):
        self._stator = Assembly()
        self._stator._partName = 'stator'
        self._stator.getChildElement(globalDict)

    def calculateCentreOfMass(self):
        return self._stator.calculateCentreOfMass()