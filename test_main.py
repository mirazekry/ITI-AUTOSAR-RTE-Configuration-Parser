
# #import the Generic TestParser Class
# from testParser import TestParser


# #Object to test the Parameter Parser
# testParamParser_1=TestParser(containerName='AdcGeneral',parserType='Parameter')

# #Object to test the Parameter Parser
# testParamParser_2=TestParser(containerName='SoAdBswModules',parserType='Parameter')

# #Object to test the Reference Parser
# testRefParser_1=TestParser(containerName='AdcGeneral',parserType='Reference')

# #Object to test the Reference Parser
# testRefParser_2=TestParser(containerName='SoAdBswModules',parserType='Reference')



# #Run all the tests of the Parameter Parser
# testParamParser_1.run()

# #Run all the tests of the Reference Parser
# testRefParser_1.run()

# #Run all the tests of the Parameter Parser
# testParamParser_2.run()

# #Run all the tests of the Reference Parser
# testRefParser_2.run()

import os
import xml.etree.ElementTree as ET

from Container.ContainerParser import ContainerParser
from Container.Container import Container

from Module.moduleParser import ModuleParser
from Module.Module import Module

from ARXMLGenerator.ARXMLGenerator import ARXMLGenerator

from Elements.Element_parser import Elements_Parser

from Major_Package.Major_Package_parser import Major_Package_Parser
from Major_Package.Major_Package import Major_Package


module = ModuleParser()
test_module= ModuleParser(moduleRootTag=module.getModule(moduleSchemaShortName='NvM'))
m=test_module.getObjects()

#objec=Major_Package_Parser()

#print('objec ',objec.shortName)


for container in m.containers:
    print("container->" + container.shortName)
    if container.parameters is not None:
        print("\t\tparameters:")
        for param in container.parameters:
            print("\t\t",param.shortName)
        print("\n")
    if container.references is not None:
        print("\t\treferences:")
        for ref in container.references:
            print("\t\t",ref.shortName)
        print("\n")
    if container.subContainers is not None:
        print("\t\tsubContainers:")
        for sub in container.subContainers:
            print("\t\t", sub.shortName)
            if sub.parameters is not None:
                print("\t\tparameters:")
                for par in sub.parameters:
                    print("\t\t",par.shortName)
            if sub.references is not None:
                print("\t\treferences:")
                for ref in sub.references:
                    print("\t\t",ref.shortName )


module_ARXML = ARXMLGenerator(m)
ARXML_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
module_ARXML.generateARXML(ARXML_file_dir)
