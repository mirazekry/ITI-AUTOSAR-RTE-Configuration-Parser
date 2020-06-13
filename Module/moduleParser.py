import xml.etree.ElementTree as ET
# Import Container module
from Module.Module import Module
from Container.Container import Container
# Import Tag module
from base.Tag import Tag
from Parameter.parameterParser import ParameterParser
from Reference.ReferenceParser import ReferenceParser
from base.BaseParser import BaseParser

from Container.ContainerParser import ContainerParser
ARXML_INPUT_FILE_PATH = 'input/AUTOSAR_MOD_ECUConfigurationParameters.arxml'
ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}


class ModuleParser(BaseParser):
    # ModuleParser class which inherits from the generic BaseParser class

    moduleRootTag = None  # Holds the container main root tag

    def __init__(self, moduleRootTag=None, arxmlNamespace=None, inputTag=Tag.inputContainer):

        # check if the moduleRootTag has a value (it must have a value)
        if moduleRootTag:
            self.moduleRootTag = moduleRootTag

        # call the base class constructor in order to assign the inherited attributes
        super().__init__(Container, moduleRootTag, arxmlNamespace, inputTag)

    def getObjects(self):
        module= Module()
        contList = []  # create an empty subcontainer list
        # Parse all the Containers using the inherited getObjects generic function
        # This will only fill the following attributes (shortName,Desc,Multiplicity) of module
        contList = super().getObjects()
        module.shortName=self.shortName
        module.description = self.description
        containerParser = ContainerParser()
        for container in contList:
            # Change the rootTag of the BaseParser to point to the current Container rootTag
            containerParser.setrootTag(container.containerRootTag)
            # Change the rootTag of the containerParser to point to the current Container rootTag
            containerParser.setContainerRootTag(container.containerRootTag)
            container.parameters, container.references, container.subContainers,container.choiceContainers = containerParser.getObjects()
            container.shortName = containerParser.shortName
            container.description = containerParser.description
        module.containers=contList
        return module

    def getAllModules(self,arxmlInputFilePath=None):
        # Function that returns All modules the arxml file
        if arxmlInputFilePath is None:
            arxmlInputFilePath=ARXML_INPUT_FILE_PATH
            
        tree = ET.parse(arxmlInputFilePath).getroot()
        All_Modules = tree.findall(
            '{http://autosar.org/schema/r4.0}AR-PACKAGES/{http://autosar.org/schema/r4.0}AR-PACKAGE/{http://autosar.org/schema/r4.0}AR-PACKAGES/{http://autosar.org/schema/r4.0}AR-PACKAGE/{http://autosar.org/schema/r4.0}ELEMENTS/{http://autosar.org/schema/r4.0}ECUC-MODULE-DEF',
            ns)
        return All_Modules




    def getModule(self,moduleSchemaShortName,arxmlInputFilePath=None):
        # Function that returns any given module root within the arxml file
        if arxmlInputFilePath is None:
            arxmlInputFilePath=ARXML_INPUT_FILE_PATH

        tree = ET.parse(arxmlInputFilePath).getroot()
        # get and return the required root
        for module in self.getAllModules():
            if module[0].text.lower() == moduleSchemaShortName.lower():
                return module




