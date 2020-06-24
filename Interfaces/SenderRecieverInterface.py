import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
from Interfaces.DataElement import DataElement
# Description : This Class contains all the sender reciever interface specifications

class SenderRecieverInterface(BaseElement):

    

    def __init__(self,Name = None,Data_Elements = []):

        super().__init__(Name)
        self.Data_Elements = []
        self.Data_Elements.extend(Data_Elements)          # Hold the Data Elements in the Interface

    def addDataElements(self,Name = None , Implementation_Type_ID = None):

        self.Data_Elements.append(DataElement(Name,Implementation_Type_ID))



