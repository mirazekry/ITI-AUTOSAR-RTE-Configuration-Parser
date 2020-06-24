import sys
sys.path.append('../')

from Base.BaseElement import BaseElement
from DataTypes.BaseType         import BaseType
# Description : This Class contains the specifications of Implementation Data types

class ImplementationDataType(BaseElement):

    value  =    'VALUE'
    struct =    'STRUCTURE'
    array  =    'ARRAY'
    union  =    'UNION'
    enums  =    'ENUM'

    Category                  = None                                # Holds the user defined DataType Category (Structure,array,value,union,enums)  
    SizeOfElements            = None                                # Holds the user defined DataType no of Elements
    arraySizeSemantics        = None                                # Holds the user defined DataType no of Elements Sematics (Fixed_size,Dynamic_size)
    arraySize                 = None


    def __init__(self,Name = None,Category = None, ReferenceType = None , Size = None):

        super().__init__(Name)
        self.ReferenceTypeID           = {}                                # Holds the user defined DataType referance type
        if Category:
            self.Category                = Category
        if ReferenceType:
            self.ReferenceTypeID[ReferenceType.split("/")[-2]]           = ReferenceType.split("/")[-1]
        if Size:
            self.SizeOfElements          = Size
        self.SubElements               = []                                  # Holds the user defined DataType Subelemnts if found



    def addSubElements(self, Name = None,Category = None, ReferenceType=None , Size = None):

        SubElementName          = None
        SubElementCategory      = None
        SubElementReferenceType = None
        SubElementSize          = None
        
        if Name:
            SubElementName           = Name
        if Category:
            SubElementCategory       = Category
        if ReferenceType:
            SubElementReferenceType  = ReferenceType
        if Size:
            SubElementSize           = Size


        self.SubElements.append(ImplementationDataType(SubElementName,SubElementCategory,SubElementReferenceType,SubElementSize))