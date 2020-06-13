
import os
import xml.etree.ElementTree as ET

#Import the Parameter Praser Class to be tested
from Parameter.parameterParser import ParameterParser

#Import the Reference Praser Class to be tested
from Reference.ReferenceParser import ReferenceParser




#Relative Path of the Input ARXML AutoSar Schema
ARXML_INPUT_FILE_PATH = 'input/AUTOSAR_MOD_ECUConfigurationParameters.arxml'
ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}




def getContainer(ContainerNamer):
    #Function that returns any given container root within the arxml file

    tree = ET.parse(ARXML_INPUT_FILE_PATH).getroot()
    containers = tree.findall(".//{Autosar}ECUC-PARAM-CONF-CONTAINER-DEF".format(**(ns)))
    
    #get and return the required root
    for container in containers:
        if container[0].text.lower() == ContainerNamer.lower():
            return container






class TestParser():
    #Generic Test Parser Class
    
    containerName = ''   #Hold the container name
    containerRoot = ''   #Holds the root of the container name
    parserType = ''      #Holds the type of parser
    parserCaller = ''    #Holds the First Parser instance
    objects = []         #Holds all the parsed object relative to the type of parser

    
    def __init__(self,containerName,parserType):
        #Class constructor

        self.containerName = containerName
        self.parserType=parserType.lower()



    def setUp(self):
        #Function which parses all the objects relative to the pre determined parser type in the constructor function

        ComConfigModuleRoot = getContainer(self.containerName)
        #get the root of the required container

        if self.parserType == 'parameter':
            self.parserCaller = ParameterParser(ComConfigModuleRoot)
            #Parameter Parser caller instance

        elif self.parserType == 'reference':
            self.parserCaller = ReferenceParser(ComConfigModuleRoot)
            #Reference Parser caller instance

        self.objects = self.parserCaller.getObjects()
        #Parse all the objects relative to the type of the parser




    def print_all_objects(self):
        #Function which prints all the data of each parsed object

        print("\n")
        for obj in self.objects:
            #iterate over all the parsed objects in the objects list
           
            print("Name: ",obj.shortName)
                #print the object short name

            print("\tMultiplicity:"+str(obj.multiplicity)+"\tValue:"+str(obj.value),end='')
                #print the object multiplicity and value (No Value added yet to the ARXML main input file)
                #proper spaces will be added to the value element in the print layout if there is a value

            if self.parserType == 'parameter':
                #check if the parser type is of Parameter Type

                print("\tType:"+str(obj.parameterType),end='')
                    #print the object parameter type
                
                if obj.parameterType == 'enum':
                    #check if the object type is enumeration

                    #print the literals list in case of enumeration type
                    print("\tEnumLiterals:{ ",end='')
                    for enum in obj.literals:
                        print(str(enum)+" ", end='')
                    print("}\n")
                else:
                    print("\n") 

            elif self.parserType == 'reference':
                #check if the parser type is of Reference Type (All Attributes is already printed)
                print("\n")        



    def get_number_objects(self):
        # Function which returns the number of the parsed objects by the determined parser

        return len(self.objects)
        #return the length of objects length



    def run(self):
        #Function which runs all the needed tests to test the determined parser

        self.setUp() 
        #Parse all the objects

        print("\n\n========================================================================")
        print("\n\nContainerNamer: "+str(self.containerName))

        if self.objects:
            #check if there are any parsed objects

            print("\n\nNumber Of "+str(self.parserType.upper())+"S = "+str(self.get_number_objects()),end='')
            #Print the number of parsed objects
            
            self.print_all_objects() 
            #Print the data of all objects
        
        else:
            print("\n\nNumber Of "+str(self.parserType.upper())+"S = 0\n")    

        print("\n\n========================================================================")
    

