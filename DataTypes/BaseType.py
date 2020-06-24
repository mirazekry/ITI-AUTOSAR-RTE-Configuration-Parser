import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
# Description : This Class contains the specifications of Software Base Data types

class BaseType(BaseElement):

    Size = None

    def __init__(self, Name = None , Size = None):

        super().__init__(Name)                    #Holds the Base DataType Name
        
        if Size:
            self.Size   =   Size                    #Holds the Base DataType size     