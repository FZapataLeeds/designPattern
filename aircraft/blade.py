class Blade:
    def __init__(self, globalDict):
        self.span = 100.0
        self.chord = 50.0
        self.thickness = 5.0
        self.leadingEdgeRad = 4.0
        self.trailingEdgeThick = 4.0
        self.density = 2.7e-6 #Aluminium density in kg/mm^3

    def calculateAerofoilSection(self):
        return self.chord*self.thickness*self.leadingEdgeRad*self.trailingEdgeThick

    def calculateCentreOfMass(self):
        volume = self.calculateAerofoilSection() * self.span
        mass = volume*self.density
        return mass
