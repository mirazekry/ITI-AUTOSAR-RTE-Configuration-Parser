import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
from Interfaces.DataElement import DataElement
# Description : This Class contains client server operations spesifications

class Operation(BaseElement):

    

    def __init__(self,Name= None):

        super().__init__(Name)

        self.Arguments          = []
        self.ArgumentsDirection = []
        self.possibleErrorsRefs = []

    def addArgument(self, ArgumentName = None , Argument_Type_ID = None, ArgumentDirection = None):

        self.Arguments.append(DataElement(ArgumentName,Argument_Type_ID))

        if ArgumentDirection:
            self.ArgumentsDirection.append(ArgumentDirection)
    
    def addPossibleErrorRef(self,possibleErrorsRef = None):

        if possibleErrorsRef:
            if type(possibleErrorsRef) == list:
                self.possibleErrorsRefs.extend(possibleErrorsRef)
            else:
                self.possibleErrorsRefs.append(possibleErrorsRef)
            
