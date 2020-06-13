
from HeaderFileClass import HeaderFile

class CFG_H(HeaderFile):

	def __init__(self,Name,filePath=None):
		self.acquire()
		super().__init__(Name,filePath)