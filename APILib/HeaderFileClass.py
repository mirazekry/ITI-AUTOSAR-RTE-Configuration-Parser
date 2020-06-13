
from FileClass import File
import testCase

class HeaderFile(File):

	def __init__(self,Name,filePath=None):

		super().__init__(Name,filePath)
		self.getFileObject().write("\n\n#ifndef "+str(self.getName()).upper()+"\n#define "+str(self.getName()).upper())


	def createMacro(self,macroPath,macroShortName=None,numberTabs=None):
		parameterInfo=self.getStructInfo(macroPath,parameter=True)
		macroSName=parameterInfo['short-name']
		macroValue=parameterInfo['value']

		if macroShortName is None:
			macroShortName=macroSName		
		if numberTabs is None:
			numberTabs=4
		if macroValue and macroShortName:
			macroPath=macroPath.split('.')	
			self.fileObject.write("#define "+str(macroPath[0]).upper()+"_"+str(macroShortName).upper()+"_PARAM"+"\t"*numberTabs+"("+str(macroValue)+"U)")	



	def closeFile(self):
		self.getFileObject().write("\n\n\n\n#endif")
		self.fileObject.close()
		super().release()



			