
#Import the Tag Module
from Tag import Tag

class BaseParser:
    #Base Parser class contains all common parsing variables and methods

    arxmlNamespace  = "{http://autosar.org/schema/r4.0}" #Holds the namespace of the AUTOSAR schema
    rootTag = None      #Holds the starting rootTag of any type (parameter,ref,container,module)
    parserClass = None  #Holds the type of parsing class of any type
    inputTag = None     #Holds the inputTag of the required objects to be parsed

    def __init__(self,parserClass,rootTag=None,arxmlNamespce=None,inputTag=None):
        #BaseParser constructor function

        #There must be a parserClass (ParameterParser,ReferenceParser,ContainerParser,ModuleParser)
        self.parserClass = parserClass

        #Assign class attributes
        if arxmlNamespce:
            self.arxmlNamespace = arxmlNamespce
        if rootTag:
            self.rootTag = rootTag
        if inputTag:
            self.inputTag = inputTag

        
    def getObjects(self,setDataTypeFunction=None):
        #Generic function which returns a list of the parsed objects

        parserObjects = None  #Holds the parsed objects starting tags
        new_object =  None    #Holds the new created object based on the parser class
        shortName =  None     #Holds the shortName starting tag
        description =  None   #Holds the description starting tag
        value =  None         #Holds the value starting tag
        moduleFlag = None     #Flag indictaes whether module/container or any other parser class type
        objectsList = []      #Holds the parsed objects lists to be returned


        #Check if the parserClass of type Module or Container(Case of subcontainers)
        if  "Module" in str(self.parserClass) or "Container" in str(self.parserClass) or "Major_Package" in str(self.parserClass):
            #set the short name
            self.shortName=(self.getShortName(self.rootTag))
            if self.shortName is not None:
                self.shortName=self.shortName.text
            #set the description
            self.description=(self.getDescription(self.rootTag))
            if self.description is not None:
                self.description=self.description.text
            #set the multiplicity
            #self.setMultiplicity(self,self.rootTag)
            #raise the module/container flag
            moduleFlag="module"

        #Get the starting root tags based on the input tag type inside the current root tag
        parserObjects = self.rootTag.find(self.arxmlNamespace+self.inputTag)
      #  print('parserObjects :',parserObjects)
        # check if the container has any inputTag (pre-determined)
        if parserObjects:
            #iterate over all the input tags
           # print('parserObjects :',parserObjects)
            for pObject in parserObjects:
                #instantiate new object of the pre-determined parserClass
             #   print('pObject :',pObject)
                new_object = self.parserClass()
                #Get the short name starting tag 
                shortName   = self.getShortName(pObject)
                #Get the discription starting tag
                description = self.getDescription(pObject)
                #Get the value starting tag (pass in case of Container/Module)
                value       = self.getValue(pObject)
                #Set all the values of the previous starting tags by extracting its texts
                self.setObject(new_object,shortName=shortName,value=value,desc=description)
                #Set the multiplicity string value
                self.setMultiplicity(new_object,pObject)
                #Set the type of the object (only in case of parameter parser, else pass)
                self.setType(new_object,pObject)
                if setDataTypeFunction:
                    setDataTypeFunction(new_object,pObject)
                #check if module/container flag set the starting rootTag    
                if moduleFlag == "module":
                    new_object.containerRootTag=pObject
                #insert the new object to the parsed objects list    
                objectsList.append(new_object)
            #return the parsed objects list
            return objectsList

        
    def getShortName(self,objectArxmlRoot):
        #Function which returns the shortname of a parser object
        return objectArxmlRoot.find(self.arxmlNamespace+Tag.inputShortName)

    def getDescription(self,objectArxmlRoot):
        #Function which returns the description of a parser object
        return objectArxmlRoot.find(self.arxmlNamespace+Tag.inputDescription)


    def setObject(self,Pobject,**kwargs):
        #Function which sets the parser object values

        #Iterate over the arguments list and get the needed text
        for key in kwargs:
            if kwargs[key] != None:
                if 'shortname' in str(key).lower():
                    Pobject.shortName = kwargs[key].text
                elif 'value' in str(key).lower():
                    Pobject.value = kwargs[key].text
                elif 'desc' in str(key).lower():
                    Pobject.description = kwargs[key][0].text
            #else:
                #print('couldn\'t find the Parser object\'s '+str(key))
    

    def setMultiplicity(self,Object,objectArxmlRoot):
        #Function which sets the multiplicity of a parser object

        lowerMul = None #Holds the value of lower multiplicity
        upperMul = None #Holds the value of upper multiplicity
        #Find the lower multiplicity
        lowerMul = objectArxmlRoot.find(self.arxmlNamespace+Tag.inputLowerMultiplicity)
        #Find the upper multiplicity
        upperMul = objectArxmlRoot.find(self.arxmlNamespace+Tag.inputUpperMultiplicity)
        #Check and get the text of the lowerMultiplicity
        if lowerMul is not None:
            lowerMul = lowerMul.text
            Object.setLowerMultiplicity(lowerMul)
        else:
            lowerMul = ''
            print('could\'n find parameter\'s lower multiplicty ')
        #Check and get the text of the lowerMultiplicity
        if upperMul is not None:
            upperMul = upperMul.text
            Object.setUpperMultiplicity(upperMul)
        else:
            upperMul = objectArxmlRoot.find(self.arxmlNamespace+Tag.inputUpperMultiplicityInfinity)
            if upperMul is not None:
                upperMul = upperMul.text
                Object.setUpperMultiplicity("Infinity")
            else :
                upperMul = ''
                print('could\'n find parameter\'s upper multiplicty ')
            
        #Map the values of the lower and upper multiplicity to pre-determined strings
        if lowerMul == '' and upperMul == '':
            Object.multiplicity = 'unknown'
        elif '0' in lowerMul :
            if 'true' in upperMul:
                Object.multiplicity = 'NoneOrInfinity'
            elif '1' in upperMul:
                Object.multiplicity = 'NoneOrOne'
        elif '1' in lowerMul:
            if 'true' in upperMul:
                Object.multiplicity = 'OneOrInfinity'
            elif '1' in upperMul:
                Object.multiplicity = 'One'


    def setrootTag(self,rootTag=None):
        #Function which sets the rootTag
        if rootTag:
            self.rootTag=rootTag


    def setType(self,Object,objectArxmlRoot):
        """ sets the type of a parser object
        this function will be doing nothing in the base class
        as it's expected to be overriten  """
        pass


    def getValue(self,objectArxmlroot):
        """Returns the value field, this function is to be overriden
           and it will be doing nothing in the base class"""
        pass
        