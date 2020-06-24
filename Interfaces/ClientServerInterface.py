import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
from Interfaces.Operation import Operation
# Description : This Class contains all the Client server interface specifications

class ClientServerInterface(BaseElement):


    def __init__(self,Name = None,Operations = []):

        super().__init__(Name)

        self.Operations = []
        self.possibleErrors = []

        if Operations:
            self.Operations.extend(Operations)
        

    def addOperation(self,Name= None):

        self.Operations.append(Operation(Name))

    
    
    def addPossibleError(self,possibleError = None):

        if possibleError:
            if type(possibleError) == list:
                self.possibleErrors.extend(possibleError)
            else:
                self.possibleErrors.append(possibleError)