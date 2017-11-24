from assembly import Assembly


class Engine:
    def __init__(self, globalDict):
        self._engine = Assembly()
        self._engine._partName = 'engine'
        self._engine.getChildElement(globalDict)

    def calculateCentreOfMass(self):
        return self._engine.calculateCentreOfMass()
