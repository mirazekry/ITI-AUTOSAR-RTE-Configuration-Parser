
class Parameter:
    #Parameter class contains all parameter's related info
    
    shortName           = None  #Holds the shortname of the parameter
    parameterType       = None  #Holds the type of the parameter
    value               = None  #Holds the value of the parameter
    multiplicity        = None  #Holds the multiplicity of the parameter
    lowerMultiplicity   = None   #Holds the lower value of multiplicity
    upperMultiplicity   = None   #Holds the upper value of multiplicity
    description         = None  #Holds the description of the parameter
    literals            = []    #In case of enum parameter its literals must be there
 
    def __init__(self,shortName=None,
                 parameterType=None,
                 value=None,
                 multiplicity=None,
                 lowerMultiplicity=None,
                 upperMultiplicity=None,
                 description=None,
                 literals=None
                 ):
        #Parameter Class constructor function

        if shortName:
            self.shortName    = shortName
        if parameterType:
            self.parameterType= parameterType
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
        if literals:
            self.literals     = literals


    def getParameterInfo(self):
        #Function which returns all parameter's info as a dict

        return {
            'short-name':self.shortName,
            'value':self.value,
            'parameterType':self.parameterType,
            'multiplicity':self.multiplicity,
            'lowerMultiplicity':self.lowerMultiplicity,
            'upperMultiplicity':self.upperMultiplicity,
            'description':self.description,
            'literals':self.literals
        }

    def setParameterType(self,parameterType):
        self.parameterType=parameterType    

    def setShortName(self,shortName):
        self.shortName=shortName

    def setValue(self,value):
        self.value=value

    def setUpperMultiplicity(self,upperMultiplicity):
        self.upperMultiplicity=upperMultiplicity

    def setLowerMultiplicity(self,lowerMultiplicity):
        self.lowerMultiplicity=lowerMultiplicity       

    def getUpperMultiplicity(self):
        return self.upperMultiplicity

    def getLowerMultiplicity(self):
        return self.lowerMultiplicity      