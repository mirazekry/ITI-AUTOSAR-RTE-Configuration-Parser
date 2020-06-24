import sys
sys.path.append('../')

from InputPathes.Tag        import Tag
from Base.BaseParser        import BaseParser
from DataTypes.BaseType               import BaseType
from DataTypes.ImplementationDataType import ImplementationDataType

# Description : This Class conatin the Parsing method for Application Elements

class ElementParser(BaseParser):
  
  AR_Package = None

  PackagesSource = [  Tag.Package,
                      Tag.inputImplementationType,
                      Tag.inputTypeCategory,
                      Tag.inputImplementationTypeElement,
                      Tag.inputArraySize,
                      Tag.inputArraySizeSemantics,
                      Tag.inputBaseTypeReference,
                      Tag.inputImplementationTypeReference,
                      Tag.inputSWbaseTypes,
                      Tag.inputBaseTypeSize ]

  def __init__(self,xmlFilePath):

    self.arxmlInputFilePath = xmlFilePath
    #Call the base class constructor to set the inherited attributes
    super().__init__()

  # This module return the needed lists for Elements parser
  def getElementPackages(self):

    ElementPackages   = {}
    ElementPackagesID = {}

    for package in self.PackagesSource:
      ElementPackages[package],ElementPackagesID[package] = self.getPackageItem(self.arxmlInputFilePath,self.arxmlNamespace,package,previousTag = None)
        
    return ElementPackages,ElementPackagesID
  
  # This module update the main package name
  def getARpackage(self):

    ElementPackages   = self.getElementPackages()[0]

    if Tag.Package in ElementPackages:
        self.AR_Package = ElementPackages[Tag.Package][0]
    return self.AR_Package

  # This module returns the parsed SW base Types and their size
  def parseBaseTypes(self):

    SWbaseTypes     =  []
    SWbaseTypesSize =  [] 
    SWbaseTypesIDs  =  []

    BaseTypes       =  []

    ElementPackages , ElementPackagesID = self.getElementPackages()

    if Tag.inputSWbaseTypes in ElementPackages:
      SWbaseTypes.extend(ElementPackages[Tag.inputSWbaseTypes])

    if Tag.inputBaseTypeSize in  ElementPackages:
      SWbaseTypesSize.extend(ElementPackages[Tag.inputBaseTypeSize])

    if Tag.inputSWbaseTypes in ElementPackagesID:
      SWbaseTypesIDs.extend(ElementPackagesID[Tag.inputBaseTypeSize])

    # creating a list of BaseType objects
    for Items in SWbaseTypesIDs:
      BaseTypes.append(BaseType(SWbaseTypes[Items],SWbaseTypesSize[Items]))

    return BaseTypes

  # This module returns the parsed Implementation Types and their related information
  def parseImplementationTypes(self):

    ImplementationDataTypes = []

    ElementPackages         = {}
    ElementPackagesID       = {}

    ElementsCategory        = []
    numberOf_subElements    = []
    subElementsCategory     = []
    subElements_counter     = 0


    ElementPackages , ElementPackagesID = self.getElementPackages()

    # splitting the Elements and subElements Category
    if Tag.inputTypeCategory                in ElementPackages:
      for item in ElementPackages[Tag.inputTypeCategory]:
        if item.isupper():
          ElementsCategory.append(item)
          numberOf_subElements.append(subElements_counter)
          subElements_counter = 0
        else:
          subElementsCategory.append(item)
          subElements_counter += 1
      numberOf_subElements.pop(0)
      numberOf_subElements.append(subElements_counter)

    # looping on the list of inputImplementationType Ids
    for Item in ElementPackagesID[Tag.inputImplementationType]:
      name           = ElementPackages[Tag.inputImplementationType][Item]
      category       = ElementsCategory[Item]
      subEle_Size    = numberOf_subElements[Item]

      if ElementPackages[Tag.inputBaseTypeReference] != []:
        Type_Ref = ElementPackages[Tag.inputBaseTypeReference].pop(0)
      else:
        Type_Ref = None
      
      # creating ImplementationDataType object for Element
      ImplementationDataTypes.append(ImplementationDataType(name,category,Type_Ref,subEle_Size))
      
      if ImplementationDataType.array in category:
        ImplementationDataTypes[Item].arraySize = ElementPackages[Tag.inputArraySize].pop(0)
        ImplementationDataTypes[Item].arraySizeSemantics = ElementPackages[Tag.inputArraySizeSemantics].pop(0)

      for subItem in range(subEle_Size):
          name      = ElementPackages[Tag.inputImplementationTypeElement].pop(0)
          category  = subElementsCategory.pop(0)
          size      = None

          
          if ElementPackages[Tag.inputImplementationTypeReference] != []:
            Type_Ref = ElementPackages[Tag.inputImplementationTypeReference].pop(0)
          else:
            Type_Ref = None
          
          # adding subElement to the Element object
          ImplementationDataTypes[Item].addSubElements(name,category,Type_Ref,size)

          if ImplementationDataType.array in category:
            ImplementationDataTypes[Item].SubElements[subItem].arraySize = ElementPackages[Tag.inputArraySize].pop(0)
            ImplementationDataTypes[Item].SubElements[subItem].arraySizeSemantics = ElementPackages[Tag.inputArraySizeSemantics].pop(0)
      
    return ImplementationDataTypes

  def getBaseTypesID(self):

    BaseTypesID = {}
    ID = 0

    for item in self.parseBaseTypes():
      BaseTypesID[item.Name] = ID
      ID += 1
      
    return BaseTypesID
    
  def getImplementationTypesID(self):

    ImplementationDataTypesID = {}
    ID = 0

    for Item in self.parseImplementationTypes():
      ImplementationDataTypesID[Item.Name] = ID
      ID += 1

    return ImplementationDataTypesID

      


    

  




#x=ElementParser('DataTypesAndInterfaces.arxml')
"""
#print(x.getElementPackages())
x.getARpackage()
print(x.AR_Package)

"""
"""s=x.parseImplementationTypes()
for i in s:
  print(i.Name,i.ReferenceTypeID,"\n")
  for w in i.SubElements:
    print(w.Name,w.ReferenceTypeID,"\n")
    for s in w.SubElements:
      print(s.Name,s.ReferenceTypeID,"\n")"""


