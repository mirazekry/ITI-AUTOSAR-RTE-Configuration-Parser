
from FileClass import File

class SourceFile(File):

	def __init__(self,Name,filePath=None):

		super().__init__(Name,filePath)

	def createStruct(self,structPath,structItems="All",parametersList=None,referencesList=None,sortList=None):
		
		containerList=self.getStructInfo(structPath)
		structString=''
		containerDepth=1

		if containerList:

			containerListOfInstances=containerList.getListOfContainerInstances()
			numberOfInstances=len(containerListOfInstances)

			if numberOfInstances > 1:
				stringLastPart="_Array["+str(len(containerListOfInstances))+"]"
			else:
				stringLastPart="_Container[1]"
				
			structString+=containerList.getShortName()+" "+containerList.getShortName()+stringLastPart+"=\n{\n"

			structString+=self.recursiveStructStringFormat(containerList=containerList,containerDepth=containerDepth)

			structString+="\n}"

		self.fileObject.write(structString)



	def createLookUpTable(self):
		pass

	def closeFile(self):
		self.fileObject.close()
		super().release()
	
	def getAllParameters(self,parametersList,containerDepth):
		structParametersString=''
		parameterInfo=None
		
		for parameter in parametersList:
			parameterInfo=parameter.getParameterInfo()
			structParametersString+="\t\t"*containerDepth+"."+str(parameterInfo['short-name'])+" = "+str(parameterInfo['value'])+"\n"	

		return structParametersString		


	def getAllReferences(self,referencesList,containerDepth):
		structReferencesString=''
		referenceInfo=None

		for reference in referencesList:
			referenceInfo=reference.getReferenceInfo()
			structReferencesString+="\t\t"*containerDepth+"."+str(referenceInfo['short-name'])+" = "+str(self.resolveRefValue(reference))+"\n"	

		return structReferencesString			


	def resolveRefValue(self,reference):
		pass	


	def recursiveStructStringFormat(self,containerList,containerDepth):	

		if containerList:
			structString=''

			containerListOfInstances=containerList.getListOfContainerInstances()
			numberOfInstances=len(containerListOfInstances)

			for containerInstance in containerListOfInstances:
				structString+="\t"*containerDepth+"{\n"

				if containerInstance.parameters:
					structString+=self.getAllParameters(parametersList=containerInstance.parameters,containerDepth=containerDepth)
				
				if containerInstance.references:
					structString+=self.getAllReferences(referencesList=containerInstance.references,containerDepth=containerDepth)

				if containerInstance.subContainers:
					for containerList in containerInstance.subContainers:
						structString+=self.recursiveStructStringFormat(containerList,containerDepth+1)

						
				structString+="\n"+"\t"*containerDepth+"}"
				if numberOfInstances > 1:
					structString+=",\n"
				numberOfInstances-=1
	

			return structString
