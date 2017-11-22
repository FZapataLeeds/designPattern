from assembly import Assembly

class Rotor:
    def __init__(self, globalDict):
        self._rotor = Assembly()
        self._rotor._partName = 'rotor'
        self._rotor.getChildElement(globalDict)

    def calculateCentreOfMass(self):
        return self._rotor.calculateCentreOfMass()
