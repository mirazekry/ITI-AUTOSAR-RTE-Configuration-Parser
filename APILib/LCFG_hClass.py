
from HeaderFileClass import HeaderFile



class LCFG_H(HeaderFile):

	def __init__(self,Name,filePath=None):
		self.acquire()		
		super().__init__(Name,filePath)

	def createMacroStructLength(self,structPath,structShortName=None,numberTabs=None):
		containerList=self.getStructInfo(structPath)
		structSName=containerList.getShortName()
		structLength=containerList.getNumberOfInstances()
		if structShortName is None:
			structShortName=structSName		
		if numberTabs is None:
			numberTabs=4
		if structLength and structShortName:
			structPath=structPath.split('.')	
			self.fileObject.write("#define "+str(structPath[0]).upper()+"_"+str(structShortName).upper()+"_CONTAINER_SIZE"+"\t"*numberTabs+"("+str(structLength)+"U)")	


	def createMacroStructIndex(self,structPath,structShortName=None,numberTabs=None):
		containerList=self.getStructInfo(structPath)
		structSName=containerList.getShortName()
		structLength=containerList.getNumberOfInstances()
		counterStructElements=None
		if structShortName is None:
			structShortName=structSName		
		if numberTabs is None:
			numberTabs=4
		if structLength and structShortName:
			structPath=structPath.split('.')
			for counterStructElements in range(int(structLength)):
				self.fileObject.write("#define "+str(structPath[0]).upper()+"_"+str(structShortName).upper()+"_ID_"+str(counterStructElements)+"\t"*numberTabs+"("+str(counterStructElements)+"U)")
				if counterStructElements != int(structLength)-1:
					self.fileObject.write("\n")	



	






