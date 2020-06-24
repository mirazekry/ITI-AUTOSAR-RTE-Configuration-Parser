import sys
sys.path.append('../')

#Tag Class which contains only all arxml common needed tags of the AUTOSAR Schema.
from InputPathes.Tag            import Tag

import xml.etree.ElementTree as ET


# Description : This class contains all common parsing variables and methods.

class BaseParser:

    CurrentARversion        = Tag('{http://autosar.org/schema/r4.0}')

    rootTag                 = None                               #Holds the starting rootTag of any type (parameter,ref,container,module)
    parserClass             = None                               #Holds the type of parsing class of any type
    inputTag                = None                               #Holds the inputTag of the required objects to be parsed
    arxmlInputFilePath      = None                               #Holds the path of the arxml file to be parsed
    arxmlNamespace          = CurrentARversion.AUTOSAR_Schema    #Holds the namespace of the AUTOSAR schema

    def __init__(self,schemaVersion=None,rootTag=None,inputTag=None,arxmlFilePath=None):

        #Assign Class Attributes
        if schemaVersion:
            self.arxmlNamespace      = schemaVersion
        if rootTag:
            self.rootTag             = rootTag
        if inputTag:
            self.inputTag            = inputTag
        if arxmlFilePath:
            self.arxmlInputFilePath  = arxmlFilePath

    # Function that returns any given Item tag within the arxml file
    def getPackageItem(self,arxmlFilePath = None, arxmlfileNameSpace = None, ItemName = None ,previousTag = None):
    
        PackageItems   = []
        PackageItemsID = []
        

        if arxmlFilePath is None:
            arxmlFilePath       = self.arxmlInputFilePath
        if arxmlfileNameSpace is None:
             arxmlfileNameSpace = self.arxmlNamespace
        
        if previousTag:
            previousTag             = self.rootTag

        if ItemName is not None:
            Item = arxmlfileNameSpace+ItemName
            allPackages,allPackagesIDs = self.getPackages(arxmlFilePath ,  previousTag)
            
            if Item in allPackages:
                if type(allPackages[Item]) == list:
                    PackageItems.extend(allPackages[Item])
                    if [] in PackageItems:
                        PackageItems.remove([])
                else:
                    PackageItems.append(allPackages[Item])

            if Item in allPackagesIDs:
                if type(allPackages[Item]) == list:
                    PackageItemsID.extend(allPackagesIDs[Item])
                    if [] in PackageItemsID:
                        PackageItemsID.remove([])
                else:
                    PackageItemsID.extend(allPackagesIDs[Item])

        return PackageItems,PackageItemsID

    # This module return all packages Data parsed from object file 
    def getPackages(self,   arxmlFilePath = None,  previousTag = None):

        retPackages         = {}
        PackageItems        = []
        retPackagesID       = {}
        tempPackageItems    = []
        retPackagescopy     = {}
        
        if arxmlFilePath is None:
            arxmlFilePath       = self.arxmlInputFilePath

        if previousTag:
            previousTag             = self.rootTag

        items = ET.parse(arxmlFilePath).getroot()
        
        for item in items.iter():
            if item.text is not None:
                if "\n" in item.text:
                    pass
                else:
                    PackageItems.clear()
                    if self.CurrentARversion.ShortName in item.tag:
                        if previousTag in retPackages : 
                            if type(retPackages[previousTag]) == list: 
                                PackageItems.extend(retPackages[previousTag])
                            else:
                                PackageItems.append(retPackages[previousTag])
                            PackageItems.append(item.text)
                            if [] in PackageItems:
                                PackageItems.remove([])
                            retPackages[previousTag]=PackageItems.copy()
                        else:
                            retPackages[previousTag]=item.text
                        
                    else:
                        if item.tag in retPackages :
                            if type(retPackages[item.tag]) == list: 
                                PackageItems.extend(retPackages[item.tag])
                            else:
                                PackageItems.append(retPackages[item.tag])
                            PackageItems.append(item.text)
                            if [] in item:
                                item.remove([])
                            retPackages[item.tag]   =   PackageItems.copy()
                        else:
                            retPackages[item.tag]   =   item.text
                        
            previousTag   =   item.tag  
        
        """ copying the packages"""
        for item in retPackages:
            if type(retPackages[item]) == list:
                retPackagescopy[item]   =   retPackages[item].copy()
            else:
                retPackagescopy[item]   =   retPackages[item]

        """ return the indicies of the list Items in Packages"""
        for Dict in retPackagescopy:
            if type(retPackagescopy[Dict]) == list:
                for item in retPackagescopy[Dict]:
                    tempPackageItems.append(retPackagescopy[Dict].index(item))
                    retPackagescopy[Dict][retPackagescopy[Dict].index(item)]    =   " "
            else:
                tempPackageItems.append(0)
            retPackagesID[Dict]    =   tempPackageItems.copy()
            tempPackageItems.clear()

        return retPackages,retPackagesID

    def getNumberOfSubItems(self,arxmlFilePath,arxmlfileNameSpace,ItemTag,SubItemsTag):

        NumberOfSubItems    =   {}

        if arxmlFilePath is None:
            arxmlFilePath       = self.arxmlInputFilePath
        if arxmlfileNameSpace is None:
            arxmlfileNameSpace  = self.arxmlNamespace

        items = ET.parse(arxmlFilePath).getroot()
        count = 0

        for item in items.iter():
            if item.tag == arxmlfileNameSpace+ItemTag:
                for subItem in item:
                    if subItem.tag == arxmlfileNameSpace+Tag.inputShortName:
                        ItemName = subItem.text
                    if subItem.tag == arxmlfileNameSpace+SubItemsTag:
                        for numberofSubItems in subItem:
                            if numberofSubItems.tag == Tag.inputShortName:
                                pass
                            else:
                                count += 1
                NumberOfSubItems[ItemName]=count
                count = 0
        return NumberOfSubItems

    def getSubElement(self,arxmlFilePath,arxmlfileNameSpace,SubElementTag):

        SubElement  =   {}
        Copy = []

        if arxmlFilePath is None:
            arxmlFilePath       = self.arxmlInputFilePath
        if arxmlfileNameSpace is None:
            arxmlfileNameSpace  = self.arxmlNamespace

        items = ET.parse(arxmlFilePath).getroot()

        for item in items.iter():

            if item.tag == arxmlfileNameSpace+Tag.inputShortName:
                ItemName    =   item.text
            if item.tag == arxmlfileNameSpace + SubElementTag:
                if '\n' in item.text:
                    for subItem in item:
                        if ItemName in SubElement:
                            if type(SubElement[ItemName]) == list:
                                Copy.extend(SubElement[ItemName])
                            else:
                                Copy.append(SubElement[ItemName])
                            Copy.append(subItem.text)
                            SubElement[ItemName]=Copy.copy()
                            Copy.clear()
                        else:
                            SubElement[ItemName] = subItem.text
                else:
                    if ItemName in SubElement:
                        if type(SubElement[ItemName]) == list:
                            Copy.extend(SubElement[ItemName])
                        else:
                            Copy.append(SubElement[ItemName])
                        Copy.append(item.text)
                        SubElement[ItemName]=Copy.copy()
                        Copy.clear()
                    else:
                        SubElement[ItemName] = item.text

        return SubElement




