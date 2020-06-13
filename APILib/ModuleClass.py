
from LCFG_cClass import LCFG_C
from LCFG_hClass import LCFG_H
from CFG_hClass import CFG_H

class Module:

	moduleName = None
	moduleNameCfg_H =  None
	moduleNameLcfg_H = None
	moduleNameLcfg_C = None
	headerFilesPath = None
	sourceFilesPath = None

	def __init__(self,moduleName,headerFilesPath=None,sourceFilesPath=None):
		self.moduleNameCfg_H =  CFG_H  (str(moduleName)+"_Cfg.h",headerFilesPath)
		self.moduleNameLcfg_H = LCFG_H (str(moduleName)+"_LCfg.h",headerFilesPath)
		self.moduleNameLcfg_C = LCFG_C (str(moduleName)+"_LCfg.c",sourceFilesPath)


	def close(self):
		self.moduleNameCfg_H.closeFile()
		self.moduleNameLcfg_H.closeFile()
		self.moduleNameLcfg_C.closeFile()

	def getFileObjects(self):
		return self.moduleNameCfg_H,self.moduleNameLcfg_H,self.moduleNameLcfg_C

	def getFileNames(self):
		return self.moduleNameCfg_H.getName(),self.moduleNameLcfg_H.getName(),self.moduleNameLcfg_C.getName()
