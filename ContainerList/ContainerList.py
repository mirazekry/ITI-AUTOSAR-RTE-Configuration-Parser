

class ContainerList:

	shortName=None
	listOfContainerInstances=[]

	def __init__(self,shortName=None,listOfContainerInstances=None):
		
		if shortName:
			self.shortName=shortName
		if listOfContainerInstances:
			self.listOfContainerInstances=listOfContainerInstances
		else:
			self.listOfContainerInstances=[]	

	def setShortName(self,shortName):
		self.shortName=shortName

	def getShortName(self):
		return self.shortName

	def setListOfContainerInstances(self,listOfContainerInstances):
		self.listOfContainerInstances=listOfContainerInstances

	def getListOfContainerInstances(self):
		return self.listOfContainerInstances

	def addInstance(self,container):
		self.listOfContainerInstances.append(container)	

	def getNumberOfInstances(self):
		return len(self.listOfContainerInstances)	

	def getContainerListInfo(self):
		return{
		'shortName': self.shortName,
		'listOfContainerInstances': self.listOfContainerInstances
		}	
	