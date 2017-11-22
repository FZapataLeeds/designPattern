import abc


class Interface(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calculateCentreOfMass(self):
        pass
