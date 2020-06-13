#new
   
class Major_Package:
 
    shortName           = None 
    containerRootTag    = None   
    Major_Package       = []    
    def __init__(self,shortName=None,
                      Major_Package=None,
                      containerRootTag= None
                 ):

        if shortName:
            self.shortName    = shortName
        if containerRootTag:
            self.containerRootTag = containerRootTag
        if Major_Package:
            self.Major_Package   = Major_Package
        else:
            self.Major_Package = []           

    def getParameterInfo(self):

        return {
            'SHORT-NAME':self.shortName,
             'ELEMENTS':self.Major_Package,
        }
   

    def setShortName(self,shortName):
        self.shortName=shortName