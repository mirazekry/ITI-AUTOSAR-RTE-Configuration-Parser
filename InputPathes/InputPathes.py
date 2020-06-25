"""import sys
sys.path.append('../')"""

class Inputs:

    DataTypesAndInterfaces_filePath     =   "./InputPathes/DataTypesAndInterfaces.arxml"
    SWC_filePath                   =   []
    
    def __init__(self,SWC_files = []):

        self.SWC_filePath.extend(SWC_files)



Inputs(["./InputPathes/SWC3.arxml"])