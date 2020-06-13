import os
from unittest import TestCase,main
from Parameter.parameterParser import ParameterParser
import xml.etree.ElementTree as ET

PROJECT_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ARXML_INPUT_FILE_PATH = os.path.join(PROJECT_BASE_DIR,'input/AUTOSAR_MOD_ECUConfigurationParameters.arxml')
# print(ARXML_INPUT_FILE_PATH)
ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}
def getContainer(ContainerNamer):
    """ a function that returns any given container root within the arxml file"""
    tree = ET.parse(ARXML_INPUT_FILE_PATH).getroot()
    containers = tree.findall(".//{Autosar}ECUC-PARAM-CONF-CONTAINER-DEF".format(**(ns)))
    for container in containers:
        if container[0].text.lower() == ContainerNamer.lower():
            return container


class TestParameterParser(TestCase):
    """ Test unit for the parameter parser"""

    def setUp(self):
        ComConfigModuleRoot = getContainer('comconfig')
        self.parameterParser = ParameterParser(ComConfigModuleRoot)
        self.parameters = self.parameterParser.getObjects()
    
    def test_getting_all_Parameter(self):
        """ Testing getting all parameters of the comConfig"""
        
        self.assertEqual(len(self.parameters),2)
    
    def test_getting_parameter_shortnames(self):
        """Testing that the shortname of a parameter is not empty and correct"""
        # for ComDataMemSize parameter
        self.assertEqual(self.parameters[0].shortName,'ComDataMemSize')
        # for ComMaxIPduCnt
        self.assertEqual(self.parameters[1].shortName,'ComMaxIPduCnt')
    
    def test_getting_the_correct_dataType(self):
        """Test that the parser sets the correct datatype for each parameter"""
        # for ComDataMemSize parameter
        self.assertEqual(self.parameters[0].parameterType,'uint64')
        # for ComMaxIPduCnt parameter
        self.assertEqual(self.parameters[1].parameterType,'uint64')
    
    def test_setting_the_expected_multiplicity(self):
        # for ComDataMemSize parameter
        self.assertEqual(self.parameters[0].multiplicity,'NoneOrOne')
        # for ComMaxIPduCnt parameter
        self.assertEqual(self.parameters[1].multiplicity,'NoneOrOne')
    
    def test_dumping_and_printing_parameter_info(self):
        for p in self.parameters:
            self.assertIsNotNone(p.getParameterInfo())
            # print(p.getParameterInfo())




if __name__ == '__main__':
    main()
