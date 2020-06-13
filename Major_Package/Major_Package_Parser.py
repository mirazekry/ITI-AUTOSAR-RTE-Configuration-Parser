#new
import xml.etree.ElementTree as ET
#Import Tag module
from Tag import Tag
#Import BaseParser module
from BaseParser import BaseParser
#import Major module
from Major_Package import Major_Package
from Element_Parser import Element_Parser


ARXML_INPUT_FILE_PATH = 'DataTypesAndInterfaces.arxml'
ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}

class Major_Package_Parser(BaseParser):
    Element_PackageRootTag = None	    
    Element_Package_ParserCaller= None
    
    def __init__(self,Major_PackageRootTag= None,arxmlNamespace=None,inputTag='AR-PACKAGES'):
		
        if Major_PackageRootTag:
            self.Major_PackageRootTag = Major_PackageRootTag

            super().__init__(Major_Package,Major_PackageRootTag,arxmlNamespace,inputTag)
        
    def getObjects(self, PackageName = None):
  
        MajorparserList=super().getObjects()
        returnList = []
        for pack in MajorparserList:
              if pack.getParameterInfo()['SHORT-NAME'] == PackageName:
                self.Element_Package_ParserCaller = Element_Parser(rootTag =pack.containerRootTag)
                ElementList=self.Element_Package_ParserCaller.getObjects()
                pack.Major_Package = ElementList
                returnList.extend(ElementList)
            
      #  print (MajorparserList[0].getParameterInfo())

        return returnList
        
        
    def getAllPackage(self,arxmlInputFilePath=None):
        # Function that returns All modules the arxml file
        if arxmlInputFilePath is None:
            arxmlInputFilePath=ARXML_INPUT_FILE_PATH
            
        tree = ET.parse(arxmlInputFilePath).getroot()
        All_Modules = tree.findall(
            '{http://autosar.org/schema/r4.0}AR-PACKAGES/{http://autosar.org/schema/r4.0}AR-PACKAGE',
            ns)
        return All_Modules
        

    def getPackage(self,moduleSchemaShortName,arxmlInputFilePath=None):
        # Function that returns any given module root within the arxml file
        if arxmlInputFilePath is None:
            arxmlInputFilePath=ARXML_INPUT_FILE_PATH

        tree = ET.parse(arxmlInputFilePath).getroot()
        # get and return the required root
        for module in self.getAllPackage():
            if module[0].text.lower() == moduleSchemaShortName.lower():
                return module


