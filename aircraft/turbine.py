from assembly import Assembly


class Turbine:
    def __init__(self, globalDict):
        self._turbine = Assembly()
        self._turbine._partName = 'turbine'
        self._turbine.getChildElement(globalDict)

    def calculateCentreOfMass(self):
        return self._turbine.calculateCentreOfMass()
