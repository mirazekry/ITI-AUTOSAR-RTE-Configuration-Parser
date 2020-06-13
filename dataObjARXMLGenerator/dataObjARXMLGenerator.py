
import os
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from base.Tag import Tag


class dataObjARXMLGenerator:
    #ARXMLGenereator class which creates ARXML file for module object
    
    Module_XML = None      #Holds the Module XML
    ModuleName = None      #Holds the Module Name
    projectName = None
    def __init__(self,Module):
        #ARXMLGenerator constructor function hich takes Module object and creates it's XML tree
        
        #create the Element tree of the module
        self.Module_XML  = ET.Element(Tag.AUTOSAR)
        self.Module_XML.set('xmlns','http://autosar.org/schema/r4.0')
        #create the first child of the Element tree(packages)
        packages = ET.SubElement(self.Module_XML, Tag.Packages)
        package = ET.SubElement(packages, Tag.Package)
        #set projectName at first as 'ProjectName'
        self.projectName = 'ProjectName'
        projectShortName = ET.SubElement(package, Tag.ShortName)
        projectShortName.text = self.projectName
        
        elements = ET.SubElement(package, Tag.Elements)
        confValues = ET.SubElement(elements, Tag.ConfValues)
        #set module shortName 
        moduleShortName = ET.SubElement(confValues, Tag.ShortName)
        moduleShortName.text = Module.shortName
        self.ModuleName = Module.shortName

        #add module containers to the tree
        moduleContainers = ET.SubElement(confValues, Tag.Containers)
        #iterate over the module containersList of instances
        for contList in Module.containers:
            
            for instanceContainer in contList.listOfContainerInstances:
            #create the container XML using createContainer_XML recursive function
                cont_XML = self.createContainer_XML(instanceContainer,contList.shortName)
                #add created container to the module tree
                moduleContainers.append(cont_XML)
            
            
    def createContainer_XML(self,cont,shortName):
    #recursive function that takes container object and creates its XML tree then return it
    
        #if container has choicecontainers List then it's a choice container  
        if cont.choiceContainers:
            #add choice container Tag to the tree
            newConfContainer = ET.Element(Tag.ConfContainerValue)
            #add container shortName
            newContainer = ET.SubElement(newConfContainer, Tag.ShortName)
            newContainer.text = cont.shortName
            #add container destination reference
            newContainer = ET.SubElement(newConfContainer, Tag.DestinationRef)
            newContainer.text = '/AUTOSAR/' + self.projectName +'/'+ self.ModuleName+ '/' + shortName
            #add choices Tag to the tree
            choiceContainersTag = ET.SubElement(newConfContainer, Tag.SubContainer)
            #iterate over the containers in choiceContainers list
            for subCont in cont.choiceContainers:
                
                for instanceContainer in subCont.listOfContainerInstances:
                    #create the choice container XML 
                    subcont_XML = self.createContainer_XML(instanceContainer,subCont.shortName)
                    ##add created choice container to the Container tree
                    choiceContainersTag.append(subcont_XML)
            
        #container is a paramConfContainer
        else:
            #add paramConf Container Tag to the tree
            newConfContainer = ET.Element(Tag.ConfContainerValue)
            #add container shortName
            newContainer = ET.SubElement(newConfContainer, Tag.ShortName)
            newContainer.text = cont.shortName
            #add container destination reference
            newContainer = ET.SubElement(newConfContainer, Tag.DestinationRef)
            newContainer.text =  '/AUTOSAR/' + self.projectName +'/'+ self.ModuleName+ '/' + shortName
            
            #check if the container has parameters
            if cont.parameters:
                #add paramaters Tag to the tree
                containerParameters = ET.SubElement(newConfContainer, Tag.ParameterValues)
                #iterate over parameters in parameters list
                for par in cont.parameters:
                    parameterXML = self.createParameterXML(par)
                    if parameterXML is not None:
                        containerParameters.append(parameterXML)
            
            #check if the container has references
            if cont.references:
                #add references Tag to the tree
                containerRefereces = ET.SubElement(newConfContainer, Tag.RefernceValue)
                #iterate over references in references list
                for ref in cont.references:
                    referenceXML = self.createReferenceXML(ref)
                    #add referenceXML 
                    containerRefereces.append(referenceXML)
                    
                    
                    
            #check if the container has subcontainers        
            if cont.subContainers:
                #add subcontainers tag to the tree
                subContainersTag = ET.SubElement(newConfContainer, Tag.SubContainer)
                #iterate over subContainers in subContainers List
                for subCont in cont.subContainers:
                    
                    for instanceContainer in subCont.listOfContainerInstances:
                    #create the subcontainer XML 
                        subcont_XML = self.createContainer_XML(instanceContainer,subCont.shortName)
                        #add the subContainer XML to the container tree
                        subContainersTag.append(subcont_XML)
                
        #return Container's  created XML tree   
        return newConfContainer
            
    def createParameterXML(self,par):
        parType = None
        #check the parameter Type and add its Tag
        if par.parameterType:
            if par.parameterType == 'boolean':
                parType = ET.Element(Tag.BooleanValue)
            elif par.parameterType == 'enum':
                parType = ET.Element(Tag.EnumerartionValue)
            elif par.parameterType == 'uint8' or par.parameterType == 'uint16' or par.parameterType == 'uint32' or par.parameterType == 'uint64':
                parType = ET.Element(Tag.NumericalValue)
            elif par.parameterType =='functionName':
                pass
            elif par.parameterType == 'float64':
                parType = ET.Element(Tag.FloatValue)
            elif par.parameterType == 'string':
                parType = ET.Element(Tag.StringValue)
                            
            if parType is not None:
                #add parameter shortName          
                parShortName = ET.SubElement(parType, Tag.ShortName)
                parShortName.text = par.shortName
                #add parameter Value
                parValue = ET.SubElement(parType, Tag.Value)
                parValue.text = par.value
                
            else:
                print('Parameter type neglected')
                
        else:
            print("No parameter type detected") 

        return parType
    
    def createReferenceXML(self,ref):
         #add reference tag
         refInfo = ET.Element(Tag.RefInfoTag)
         #add reference shortName
         refShortName = ET.SubElement(refInfo, Tag.ShortName)
         refShortName.text = ref.shortName
         #add reference destination
         refDestination = ET.SubElement(refInfo, Tag.DestinationRef)
         refDestination.text = ref.value
         
         return refInfo
        
    def setProjectName(self,newName):
         #set the name of the project      
        '''it should get the first shortName which is correct but need to be tested'''
        projectShortName = self.Module_XML.find(Tag.ConfValues)
        projectShortName.text = newName


              
        
    def generateARXML(self,ARXML_file_dir):
        #funcation takes the directory and creates the ARXML file in it

        completeName = os.path.join(ARXML_file_dir,self.ModuleName + ".arxml")
        self.Module_XML = ET.tostring(self.Module_XML)
        self.Module_XML = parseString(self.Module_XML)
        self.Module_XML = self.Module_XML.toprettyxml()
        #file1.write(ET.tostring(self.Module_XML,encoding="unicode"))
        file1 = open(completeName, "w")
        file1.write(self.Module_XML)
        file1.close()






