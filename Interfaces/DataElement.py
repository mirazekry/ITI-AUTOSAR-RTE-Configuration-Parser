import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
# Description : This Class contains DataElement specifications 

class DataElement(BaseElement):

    Implementation_Type_ID = None

    def __init__(self,Name = None , Implementation_Type_ID = None):

        super().__init__(Name)
        
        self.Implementation_Type_ID = Implementation_Type_ID
