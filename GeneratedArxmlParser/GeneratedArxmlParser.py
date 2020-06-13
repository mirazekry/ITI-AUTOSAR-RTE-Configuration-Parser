

import sys
sys.path.append('../Module')
sys.path.append('../Container')
sys.path.append('../Parameter')
sys.path.append('../Reference')
sys.path.append('../ContainerList')

import xml.etree.ElementTree as ET
import xmltodict

from Module import Module
from Container import Container
from ContainerList import ContainerList
from parameter 	import Parameter
from Reference import Reference


class GeneratedArxmlParser:

	moduleDataObject=None
	
	def __init__(self,filepath=None,fileObject=None):

		if filepath:
			genArxmlFileObject=open(filepath)
		elif fileObject:
			genArxmlFileObject=fileObject
		else:
			raise Exception("No, Filepath/FileObject found")	

		dataObjectDict = xmltodict.parse(genArxmlFileObject.read())

		self.moduleDataObject = self.dictToModuleDataObject(dataObjectDict)

		genArxmlFileObject.close()


	def getModuleDataObject(self):
		return self.moduleDataObject


	def getParametersOrReferences(self,listDict,parameters=None,references=None):
	
		if listDict:
			listDataObjects=[]
			objectClass=None
			dictionaryValueKey=None
			elementDataObject=None
			elementDict=None
			
			if parameters:
				objectClass=Parameter
				dictionaryValueKey='VALUE'
			elif references:
				objectClass=Reference
				dictionaryValueKey='DESTINATION-REF'	

			for elementKey in listDict:	
				elementsList = []

				if type(listDict[elementKey]) != list:
					elementsList.append(dict(listDict[elementKey]))
				else:
					elementsList=listDict[elementKey]	

				for element in elementsList:
					elementDataObject=objectClass(shortName=element['SHORT-NAME'],value=element[dictionaryValueKey])
					if parameters:
						elementKeyParsedList=elementKey.split('-')	
						elementDataObject.setParameterType(elementKeyParsedList[1].lower())
					listDataObjects.append(elementDataObject)
						
			return listDataObjects	


	def dictToModuleDataObject(self,dataObjectDict):

		if dataObjectDict:
			moduleShortName=dataObjectDict['AUTOSAR']['AR-PACKAGES']['AR-PACKAGE']['ELEMENTS']['ECUC-MODULE-CONFIGURATION-VALUES']['SHORT-NAME']

			containersList=dataObjectDict['AUTOSAR']['AR-PACKAGES']['AR-PACKAGE']['ELEMENTS']['ECUC-MODULE-CONFIGURATION-VALUES']['CONTAINERS']['ECUC-PARAM-CONF-CONTAINER']

			containerListOfLists=self.dictToContainerDataObject(containersList=containersList)

			moduleDataObject=Module(shortName=moduleShortName,containers=containerListOfLists)

		return moduleDataObject




	def dictToContainerDataObject(self,containersList):
		if containersList:
			containerListOfLists=[]
			subContainerListOfLists=[]
			destRefPrevious=None

			for container in containersList:
				parametersListDataObj=[]
				referencesListDataObj=[]

				containerDataObject=Container(shortName=container['SHORT-NAME'])

				if 'PARAMETER-VALUES' in container:
					parametersListDataObj=self.getParametersOrReferences(listDict=container['PARAMETER-VALUES'],parameters=True)
					containerDataObject.setParameters(parametersListDataObj)

				if 'REFERENCE-VALUES' in container:
					referencesListDataObj=self.getParametersOrReferences(listDict=container['REFERENCE-VALUES'],references=True)
					containerDataObject.setReferences(referencesListDataObj)

				if 'SUB-CONTAINERS' in container:
					subContainerslist=[]
					
					if type(container['SUB-CONTAINERS']['ECUC-PARAM-CONF-CONTAINER']) != list:
						subContainerslist.append(container['SUB-CONTAINERS']['ECUC-PARAM-CONF-CONTAINER'])
					else:
						subContainerslist=container['SUB-CONTAINERS']['ECUC-PARAM-CONF-CONTAINER']

					subContainerListOfLists=self.dictToContainerDataObject(subContainerslist)
					containerDataObject.setSubContainers(subContainerListOfLists)
					
				if container['DESTINATION-REF'] != destRefPrevious:
					destRefPrevious=container['DESTINATION-REF']
					destReferenceParsedlist=destRefPrevious.split('/')
					containerList=ContainerList(shortName=destReferenceParsedlist[-1])
					if destRefPrevious is not None:
						containerListOfLists.append(containerList)
	
				containerList.addInstance(containerDataObject)

			return containerListOfLists	




#####################################################################################

#To Run The GeneratedArxmlParser Class use:

# Parser_1=GeneratedArxmlParser(filepath='../Requirements/required.arxml')
# moduleDataObject_1=Parser_1.getModuleDataObject()

# Parser_2=GeneratedArxmlParser(filepath='../Requirements/NvM.arxml')
# moduleDataObject_2=Parser_2.getModuleDataObject()

# Parser_3=GeneratedArxmlParser(filepath='../Requirements/SoAd.arxml')
# moduleDataObject_3=Parser_3.getModuleDataObject()


# or

# fileObject=open('../Requirements/required.arxml')
# Parser=GeneratedArxmlParser(fileObject=fileObject)
# moduleDataObject=Parser.getModuleDataObject()

#####################################################################################



#TEST

# print("\n")
# print(moduleDataObject.containers[0].shortName)
# print(moduleDataObject.containers[0].listOfContainerInstances[0].parameters)
# print(moduleDataObject.containers[0].listOfContainerInstances[1].parameters)
# print("\n")
# print(moduleDataObject.containers[1].shortName)
# print(moduleDataObject.containers[1].listOfContainerInstances[0].parameters)
# print("\n")
#print(moduleDataObject.containers[2].shortName)
#print(moduleDataObject.containers[2].listOfContainerInstances[0].references)
#print(moduleDataObject.containers[0].listOfContainerInstances[0].subContainers[0].listOfContainerInstances[0].parameters[28].parameterType)





	