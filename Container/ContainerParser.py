
import xml.etree.ElementTree as ET
#Import Container module
from Container.Container import Container
#Import Tag module
from base.Tag import Tag
#Import ParameterParser module
from Parameter.parameterParser import ParameterParser
#Import ReferenceParser module
from Reference.ReferenceParser import ReferenceParser
#Import BaseParser module
from base.BaseParser import BaseParser

#Relative Path of the Input ARXML AutoSar Schema
ARXML_INPUT_FILE_PATH = 'input/AUTOSAR_MOD_ECUConfigurationParameters.arxml'
ns = {'Autosar':'{http://autosar.org/schema/r4.0}'}



class ContainerParser(BaseParser):
	#ContainerParser class which inherits from the generic BaseParser class

	containerRootTag = None 	#Holds the container main root tag
	paramParserCaller =  None	#Holds the parameter parser object
	refParserCaller =  None 	#Holds the reference parser object
	parserObjects=	 None	    #Holds all the sub-container parsed objects



	def __init__(self,containerRootTag=None,arxmlNamespace=None,inputTag=None):
		#ContainerParser constructor function

		#check if the containerRootTag has a value (it must have a value)
		if containerRootTag:
			self.containerRootTag = containerRootTag
		

		#call the base class constructor in order to assign the inherited attributes
		super().__init__(Container,containerRootTag,arxmlNamespace,inputTag)
		

	def getObjects(self):
		#Function which parses parametersList,referencList and subContainerList including thier parametersList and referenceList
		
		containerParser = None	#Holds an object of the containerParser class (self class)
		subContList = [] 		#create an empty subcontainer list
		
		#Instantiate a ParameterParser object using pre-determined containerRootTag
		self.paramParserCaller = ParameterParser(self.containerRootTag)

		#Instantiate a ReferenceParser object using pre-determined containerRootTag
		self.refParserCaller = ReferenceParser(self.containerRootTag)
        
		#Set container's inputTag to subContainers Tag to parse all the subContainers
		self.inputTag = Tag.inputSubContainer
		#Parse all the subContainers using the inherited getObjects generic function
		#This will only fill the following attributes (shortName,Desc,Multiplicity) of each Container
		subContList = super().getObjects()
        
		#Set container's inputTag to Choices Tag to parse all the choicesContainers(in case container )
		self.inputTag = Tag.Choices
		#Parse all the subContainers using the inherited getObjects generic function
		#This will only fill the following attributes (shortName,Desc,Multiplicity) of each Container
		choicesContList = super().getObjects()

		#Check if there any subcontainers in this container
		if subContList:
			#Instantiate a ContainerParser object (self class) in order to apply recursion
			containerParser = ContainerParser()
			#iterate over the subcontainer list
			for subContainer in subContList:    
				#Change the rootTag of the BaseParser to point to the current subContainer rootTag
				containerParser.setrootTag(subContainer.containerRootTag)
				#Change the rootTag of the containerParser to point to the current subContainer rootTag
				containerParser.setContainerRootTag(subContainer.containerRootTag)
				#Call the same function again, and get the parameters,references,subContainers lists,choiceContainerLists
				subContainer.parameters,subContainer.references,subContainer.subContainers,subContainer.choiceContainers = containerParser.getObjects()	
        
		#Check if there is any choiceContainers in this container
		if choicesContList:
			#Instantiate a ContainerParser object (self class) in order to apply recursion
			containerParser = ContainerParser()
			#iterate over the choices container list
			for choiceContainer in choicesContList:
                
				#Change the rootTag of the BaseParser to point to the current subContainer rootTag
				containerParser.setrootTag(choiceContainer.containerRootTag)
				#Change the rootTag of the containerParser to point to the current subContainer rootTag
				containerParser.setContainerRootTag(choiceContainer.containerRootTag)
				#Call the same function again, and get the parameters,references,subContainers lists,choiceContainerLists
				choiceContainer.parameters,choiceContainer.references,choiceContainer.subContainers,choiceContainer.choiceContainers = containerParser.getObjects()	
		
		#return the four parsed lists
		return self.paramParserCaller.getObjects(), self.refParserCaller.getObjects(),subContList,choicesContList

	def getContainer(self,containerSchemaShortName):
		# Function that returns any given container root within the arxml file
		tree = ET.parse(ARXML_INPUT_FILE_PATH).getroot()
		containers = tree.findall(".//{Autosar}ECUC-PARAM-CONF-CONTAINER-DEF".format(**(ns)))

		# get and return the required root
		for container in containers:
			if container[0].text.lower() == containerSchemaShortName.lower():
				return container

	def getContainerRootTag(self):
		#Function which returns the containerRootTag
		return self.containerRootTag


	def setContainerRootTag(self,containerRootTag=None):
		#Function which sets the containerRootTag
		if containerRootTag:
			self.containerRootTag = containerRootTag
