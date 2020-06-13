class Reference:
    #Reference class contains all reference's related info
    
    shortName           = None    #Holds the shortname of the reference
    value               = None    #Holds the value of the reference
    multiplicity        = None    #Holds the multiplicity of the reference
    lowerMultiplicity   = None   #Holds the lower value of multiplicity
    upperMultiplicity   = None   #Holds the upper value of multiplicity
    description         = None    #Holds the description of the reference
    referenceType       = None
    referenceChoices    = []


    def __init__(self,shortName=None,
                 value=None,
                 multiplicity=None,
                 lowerMultiplicity=None,
                 upperMultiplicity=None,
                 description=None,
                 referenceType=None,
                 referenceChoices=None
                 ):
        #Reference class constructor Function
        if shortName:
            self.shortName    = shortName
        if value:
            self.value        = value
        if multiplicity:
            self.multiplicity = multiplicity
        if lowerMultiplicity:
            self.lowerMultiplicity=lowerMultiplicity
        if upperMultiplicity:
            self.upperMultiplicity=upperMultiplicity    
        if description:
            self.description  = description
        if referenceType:
            self.referenceType=referenceType
        if referenceChoices:
            self.referenceChoices=referenceChoices        
       
    def setShortName(self,shortName):
        self.shortName=shortName
           
    def setReferenceType(self,referenceType):
        self.referenceType=referenceType   

    def setReferenceValue(self,value):
        self.value=value

    def setReferenceChoices(self,referenceChoices):
        self.referenceChoices=referenceChoices    

    def getReferenceInfo(self):
        #Function which returns all Refernce's info as a dict"""

        return {
            'short-name':self.shortName,
            'value':self.value,
            'multiplicity':self.multiplicity,
            'lowerMultiplicity':self.lowerMultiplicity,
            'upperMultiplicity':self.upperMultiplicity,
            'description':self.description,
            'referenceType':self.referenceType,
            'referenceChoices':self.referenceChoices
        }


    def setUpperMultiplicity(self,upperMultiplicity):
        self.upperMultiplicity=upperMultiplicity

    def setLowerMultiplicity(self,lowerMultiplicity):
        self.lowerMultiplicity=lowerMultiplicity    

    def getUpperMultiplicity(self):
        return self.upperMultiplicity

    def getLowerMultiplicity(self):
        return self.lowerMultiplicity