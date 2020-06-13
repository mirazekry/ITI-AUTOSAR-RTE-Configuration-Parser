
import testCase

class File:

	Name = None
	fileObject= None
	filePath= 'GeneratedFiles/'
	codeBinarySemaphore = True


	def __init__(self,Name,filePath=None):
		
		if filePath:
			self.filePath=filePath

		self.fileObject=open(self.filePath+Name,"w+")

		Name=Name.replace(".","_")
		Name=Name[:-1]+Name[-1].upper()
		self.Name = Name
		

	def setName(self,Name):
		self.Name = Name

	def getName(self):
		return self.Name	


	def getFileObject(self):
		return self.fileObject

	def writeNewLine(self,numberLines=None):
		if numberLines is None:
			numberLines=1
		self.fileObject.write("\n"*numberLines)

	def writeCommentLine(self,comment):
		comment=comment.replace('\n','')
		self.fileObject.write("/* "+str(comment)+" */")

	def writeCommentMulLine(self,comment,section=None):
		if section:
			self.fileObject.write("/"+"*"*90+"\n")
			commentList=comment.split('\n')
			for comLine in commentList:
				comLineLength=len(comLine)
				astriskLength=int((91-comLineLength)/2)		
				self.fileObject.write("*"*astriskLength+str(comLine)+"*"*astriskLength+"\n")
			self.fileObject.write("*"*90+"/")
		else:	
			comment=comment.replace('\n','\n* ')
			self.fileObject.write("/*\n* "+str(comment)+"\n*/")
	
	@classmethod
	def acquire(cls):
		if cls.codeBinarySemaphore == True :
			cls.codeBinarySemaphore = False
		else:
			raise Exception("Error, Creating module within another module")	

	@classmethod
	def release(cls):
		if cls.codeBinarySemaphore == False:
			cls.codeBinarySemaphore = True
		else:
			raise Exception("Error,Module is not acquired to be released")	



	def getStructInfo(self,structPath,parameter=None):	
		pathList=structPath.split('.')
		modifiedstructPath=structPath[structPath.find('.')+1:]
		for module in testCase.modulesList:
			if (module.getModuleInfo())['short-name'] == pathList[0]:
				return self.recursiveStructInfo(modifiedstructPath,(module.getModuleInfo())['containers'],parameter)



	def recursiveStructInfo(self,structPath,containerListOfLists,parameter=None):
		
		pathList=structPath.split('.')
		modifiedstructPath=None
		for containerList in containerListOfLists:
			if containerList.getShortName() == pathList[0]:
				if len(pathList) == 1:	
					return containerList
				else:
					modifiedstructPath=structPath[structPath.find('.')+1:]
					modifiedstructPath=modifiedstructPath[modifiedstructPath.find('.')+1:]
					for containerInstance in containerList.getListOfContainerInstances():
						if (containerInstance.getContainerInfo())['short-name'] == pathList[1]:
							if parameter and len(pathList) == 3:
								for parameter in containerInstance.parameters:
									parameterInfo=parameter.getParameterInfo()
									if parameterInfo['short-name'] == pathList[2]:
										return parameterInfo
							else:	
								return self.recursiveStructInfo(modifiedstructPath,(containerInstance.getContainerInfo())['subContainers'])