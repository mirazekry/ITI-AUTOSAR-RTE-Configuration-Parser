
#Import Parameter module
from Parameter.parameter import Parameter
#Import Tag module
from base.Tag import Tag
#Import BaseParser module
from base.BaseParser import BaseParser


class ParameterParser(BaseParser):
    #ParameterParser class that should parse and return all container's parameter's info

    def __init__(self,containerRoot=None,arxmlNamespace=None,inputTag=Tag.inputParameters):
        #Class constructor function which inits and accepts the container's arxml reference

        #Call the base class constructor to set the inherited attributes
        super().__init__(Parameter,containerRoot,arxmlNamespace,inputTag)
    

    
    def getObjects(self,setDataTypeFunction=None):
        """Function which overrides the base get objects function and send a reference to function so 
        each parameter datatype can be set according to the setParameterType function"""
        return super().getObjects(self.setParameterType)


    def setParameterType(self,Pobject,parameterArxmlRoot):
        #Function which sets the parameter type depending on its max, and min tags

        #check on the type of parameter based on the string of the rootTag
        if 'boolean' in parameterArxmlRoot.tag.lower():
            Pobject.parameterType = 'boolean'
        elif 'enumeration' in parameterArxmlRoot.tag.lower():
            Pobject.parameterType = 'enum'
            # we must set the parameters literls so we can list possible values to the user
            Pobject.literals = self.getParameterLiterals(parameterArxmlRoot)
        elif 'string' in parameterArxmlRoot.tag.lower():
            Pobject.parameterType = 'string'
        elif 'function' in parameterArxmlRoot.tag.lower():
            Pobject.parameterType = 'functionName'
        elif 'integer' in parameterArxmlRoot.tag.lower():
            minValue = parameterArxmlRoot.find(self.arxmlNamespace+'MIN')
            if minValue is not None:
                minValue = minValue.text
            maxValue = parameterArxmlRoot.find(self.arxmlNamespace+'MAX')
            if maxValue is not None:
                maxValue = maxValue.text
            #Get the integer type based on the mini and max values    
            Pobject.parameterType = self.getIntType(minValue,maxValue)
        elif 'float' in parameterArxmlRoot.tag.lower():
              Pobject.parameterType = 'float64'
    
    
    def getIntType(self,minR,maxR):
        #Helper functions helps to detect integer length
        
        minRange = None    #Minimum value
        maxRange = None    #Maximum value
        
        try:
            minRange =int(minR)
            maxRange = int(maxR)
            
            #Check the range
            if minRange >= 0:
                if maxRange <= 255:
                    return 'uint8'
                elif maxRange <= 65535:
                    return 'uint16'
                elif maxRange <= 4294967295:
                    return 'uint32'
                elif maxRange <= 18446744073709551615:
                    return 'uint64'
        except: 
            print("integer range conversion error")
            return 'uint64'
    
    def getParameterLiterals(self,parameterArxmlroot):
        #Helper function that returns all literals values for parameter of type Enumeration (Only)
        
        literalsValue=[] #Holds all the literal values of an enum
        literals = None  #Hold the starting tag of each value

        #Get all the starting tags of the enum literal values
        literals = parameterArxmlroot.findall(".//{}ECUC-ENUMERATION-LITERAL-DEF".format(self.arxmlNamespace))
        #iterate on each tag
        for literal in literals:
            #get the short name starting tag of the current literal
            literalShortName = literal.find("{}{}".format(self.arxmlNamespace,Tag.inputShortName))
            if literalShortName is not None:
                #add the literal shortname text to the literalsValue list
                literalsValue.append(literalShortName.text)
        #return the literalsValue list
        return literalsValue


    def getValue(self,objectArxmlroot):
        #Function which overrides a base class virtual function to get the parameter value
        return objectArxmlroot.find(self.arxmlNamespace+Tag.generationValue)



