#new
#Import Tag module
from Tag import Tag
#Import BaseParser module
from BaseParser import BaseParser
from Element import Element

#ARXML_INPUT_FILE_PATH = 'input/DataTypesAndInterfaces.arxml'
#ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}

class Element_Parser(BaseParser):
    #Element_Parser class that should parse and return all container's parameter's info
        
    def __init__(self,rootTag=None,arxmlNamespace=None,inputTag='ELEMENTS'):
        

        #Call the base class constructor to set the inherited attributes
        super().__init__(Element,rootTag,arxmlNamespace,inputTag)
    
    def getObjects(self):
  
        E= super().getObjects()
        """
        for i in E:
            print(i.getParameterInfo())
        """
        return E  
       

        
