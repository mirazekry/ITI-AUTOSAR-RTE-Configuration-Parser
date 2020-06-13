class Module:
    shortName = None
    description= None
    multiplicity = None
    lowerMultiplicity   = None   #Holds the lower value of multiplicity
    upperMultiplicity   = None   #Holds the upper value of multiplicity
    containers = []

    def __init__(self,shortName=None,
                 description=None,
                 multiplicity=None,
                 lowerMultiplicity=None,
                 upperMultiplicity=None,
                 containers=None):

        if shortName:
            self.shortName = shortName
        if description:
            self.descrription = description
        if multiplicity:
            self.multiplicity = multiplicity
        if lowerMultiplicity:
            self.lowerMultiplicity=lowerMultiplicity
        if upperMultiplicity:
            self.upperMultiplicity=upperMultiplicity    
        if containers:
            self.containers  = containers
        else:
            self.containers=[]    

    def setShortName(self,shortName):
        self.shortName=shortName

    def setContainersList(self,containers):
        self.containers=containers    

    def getModuleInfo(self):
    # Function which returns all container's info as a dict
      return {
        'short-name': self.shortName,
        'multiplicity': self.multiplicity,
        'lowerMultiplicity':self.lowerMultiplicity,
        'upperMultiplicity':self.upperMultiplicity,
        'description': self.description,
        'containers': self.containers,
    }


    def setUpperMultiplicity(self,upperMultiplicity):
        self.upperMultiplicity=upperMultiplicity

    def setLowerMultiplicity(self,lowerMultiplicity):
        self.lowerMultiplicity=lowerMultiplicity

    def getUpperMultiplicity(self):
        return self.upperMultiplicity

    def getLowerMultiplicity(self):
        return self.lowerMultiplicity