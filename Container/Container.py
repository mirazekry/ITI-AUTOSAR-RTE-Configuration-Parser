

class Container:
    #Container class contains all container's related info

    shortName        = None   #Holds the shortname of the container object
    multiplicity     = None   #Holds the multiplicity of the container object
    lowerMultiplicity= None   #Holds the lower value of multiplicity
    upperMultiplicity= None   #Holds the upper value of multiplicity
    description      = None   #Holds the description of the container object
    codeParent       = None   #Holds the codeParent of the container object
    containerRootTag = None   #Holds the containerRootTag of the container object
    parameters       = []     #Holds the parameters which belong to this container object
    references       = []     #Holds the references which belong to this container object
    subContainers    = []     #Holds the subContainers which belong to this container object
    choiceContainers = []     #Holds te choiceContainers in case container was choice-container
    def __init__(self,shortName=None,
                 multiplicity=None,
                 lowerMultiplicity=None,
                 upperMultiplicity=None,
                 description=None,
                 codeParent=None,
                 parameters=None,
                 references=None,
                 subContainers=None,
                 choiceContainers=None,
                 containerRootTag=None
                 ):
        #Container class constructor function

        if shortName:
            self.shortName    = shortName
        if multiplicity:
            self.multiplicity = multiplicity
        if lowerMultiplicity:
            self.lowerMultiplicity=lowerMultiplicity
        if upperMultiplicity:
            self.upperMultiplicity=upperMultiplicity    
        if description:
            self.description  = description
        if codeParent:
            self.codeParent   = codeParent
        if parameters:
            self.parameters   = parameters
        else:
            self.parameters = []    
        if references:
            self.references   = references
        else:
            self.references = []    
        if subContainers:
            self.subContainers = subContainers
        else:
            self.subContainers = []    
        if choiceContainers:
            self.choiceContainers = choiceContainers
        if containerRootTag:
            self.containerRootTag= containerRootTag
            
    def getContainerInfo(self):
        #Function which returns all container's info as a dict

        return {
            'short-name':self.shortName,
            'multiplicity':self.multiplicity,
            'lowerMultiplicity':self.lowerMultiplicity,
            'upperMultiplicity':self.upperMultiplicity,
            'description':self.description,
            'codeParent':self.codeParent,
            'parameters':self.parameters,
            'references':self.references,
            'subContainers':self.subContainers,
            'choiceContainers':self.choiceContainers,
            'containerRootTag':self.containerRootTag
        }
    

    def addContainer(self,subContainer):
        #Function which adds a new subcontainer to the subContainers list
        self.subContainers.append(subContainer)

    def removeContainer(self,inputco=None):
        #Function which removes a container from the subContainers list
        if type(inputco) is int:
            self.subContainers.pop(inputco)
        elif type(inputco) is str:
            for index, fi in enumerate(self.subcontainers):
                if fi.shortname == inputco:
                    self.subContainers.pop(index)
                    break


    def getParamterType(self,inputpr=None):
        if type(inputpr) is int:
            return self.parameters[inputpr].parameterType
        elif type(inputpr) is str:
            for index, fi in enumerate(self.parameters):
                if fi.shortname == inputpr:
                    return self.parameters[index].parameterType

    def updataContainer(self,newcontainer,indexcont):
        if type(indexcont) is int:
            self.subContainers[indexcont] = newcontainer
        elif type(indexcont) is str:
            for index, fi in enumerate(self.subcontainers):
                if fi.shortname == indexcont:
                    self.subContainers[index] = newcontainer


        
    def setShortName(self,shortName):
        self.shortName=shortName

    def setParameters(self,parameters):
        self.parameters=parameters

    def setReferences(self,references):
        self.references=references     

    def setSubContainers(self,subContainers):
        self.subContainers=subContainers                   
        
    def setUpperMultiplicity(self,upperMultiplicity):
        self.upperMultiplicity=upperMultiplicity

    def setLowerMultiplicity(self,lowerMultiplicity):
        self.lowerMultiplicity=lowerMultiplicity

    def getUpperMultiplicity(self):
        return self.upperMultiplicity

    def getLowerMultiplicity(self):
        return self.lowerMultiplicity