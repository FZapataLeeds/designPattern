from assembly import Assembly
from toolbox import *


if __name__ == '__main__':
    defaultDict = LookUpBOM.lookupbom('bom.txt')
    aircraft = Assembly()
    aircraft._partName = 'aircraft'
    aircraft.getChildElement(defaultDict)

    print("Aircraft has {} main parts".format(aircraft.__len__()))
    print("Total mass of Aircraft is {} kg".format(aircraft.calculateCentreOfMass()))
