import sys
sys.path.append('../')

from Base.BaseElement import BaseElement 

# Description : This class contain ports specifications

class Port(BaseElement):

    def __init__(self,Name , Port_Type , Interface_Type ,Interface_ID):

        super().__init__(Name)

        self.Port_Type              = None
        self.Interface_Type         = None
        self.Interface_ID           = None

        if Port_Type:
            self.Port_Type          = Port_Type
        if Interface_Type:
            self.Interface_Type     = Interface_Type
        if Interface_ID:
            self.Interface_ID       = Interface_ID

        if self.Interface_Type == 'Sender_Reciever_Interface':
            self.Port_DataElement       = None
        elif self.Interface_Type == 'Client_Server_Interface':
            self.Port_Operation         = None

    def addDataElement(self,DE = None):

        self.Port_DataElement = DE

    def addOperation(self,OP = None):

        self.Port_Operation = OP



