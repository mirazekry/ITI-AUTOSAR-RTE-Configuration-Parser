
#Import the Reference module
from Reference.Reference import Reference
#Import BaseParser module
from base.BaseParser import BaseParser
#Import Tag module
from base.Tag import Tag

class ReferenceParser(BaseParser):
	#ReferenceParser class that should parse and return all container's reference's info

    def __init__(self,containerRoot=None,arxmlNamespace=None,inputTag=Tag.inputReferences):
        #ReferenceParser constructor function which inits and accepts the container's arxml reference

        #Call the base class constructor to set the inherited attributes
        super().__init__(Reference,containerRoot,arxmlNamespace,inputTag)
    

    def getObjects(self,setReferenceTypeFunction=None):
    	return super().getObjects(self.setReferenceType)


    def setReferenceType(self,Pobject,parameterArxmlRoot):
        rootTagString=parameterArxmlRoot.tag.lower()

        if 'symbolic' in rootTagString:
            Pobject.setReferenceType("symbolicReference")
        elif 'foreign'in rootTagString:
            Pobject.setReferenceType("foreignReference")
            Pobject.setReferenceValue(parameterArxmlRoot.find(self.arxmlNamespace+'DESTINATION-TYPE').text)
        elif 'choice' in rootTagString:
            Pobject.setReferenceType("choiceReference")
            Pobject.setReferenceChoices(self.getReferenceLiterals(parameterArxmlRoot))
        elif 'instance' in rootTagString:
            Pobject.setReferenceType("instanceReference")
            Pobject.setReferenceValue(parameterArxmlRoot.find(self.arxmlNamespace+'DESTINATION-TYPE').text)
        else:
            Pobject.setReferenceType("reference")                    

    def getReferenceLiterals(self,parameterArxmlRoot):
    	referenceLiterals = []
    	literalsRootTag   = None

    	literalsRootTag = parameterArxmlRoot.find(self.arxmlNamespace+'DESTINATION-REFS')
    	if literalsRootTag:
    		for literal in literalsRootTag:
    			referenceLiterals.append(literal.text)

    	return referenceLiterals

    def getValue(self,objectArxmlroot):
        #Function which overrides a base class virtual function to get the reference value
        return objectArxmlroot.find(self.arxmlNamespace+Tag.inputReferenceDestRef) 

    