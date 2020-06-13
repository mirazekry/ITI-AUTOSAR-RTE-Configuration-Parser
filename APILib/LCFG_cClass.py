
from SourceFileClass import SourceFile

class LCFG_C(SourceFile):

	def __init__(self,Name,filePath=None):
		self.acquire()
		super().__init__(Name,filePath)
