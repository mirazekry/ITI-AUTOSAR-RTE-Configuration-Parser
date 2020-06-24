import sys
sys.path.append('../')

from InputPathes.Tag                        import Tag
from DataTypes.BaseType                     import BaseType
from Interfaces.Operation                              import Operation
from Base.BaseParser                        import BaseParser
from Interfaces.DataElement                            import DataElement
from DataTypes.ElementsParser               import ElementParser
from Interfaces.ClientServerInterface       import ClientServerInterface
from DataTypes.ImplementationDataType       import ImplementationDataType
from Interfaces.SenderRecieverInterface     import SenderRecieverInterface

class InterfaceParser(BaseParser):

    PackagesSource = [  Tag.inputSenderRecieverInterface,
                        Tag.inputSRDataElement,
                        Tag.inputTypeReference,
                        Tag.inputClientServerInterface,
                        Tag.inputCSOperation,
                        Tag.inputOpArgument,
                        Tag.inputOpArgumentDirection,
                        Tag.inputPossibleError,
                        Tag.inputPossibleErrorRef   ]


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

    def getTypeRefID(self):

        SR_dataElement_TypeRefID    = []
        CS_opArgument_TypeRefID     = []

        TypeRefs                    = []
        SR_dataElement_TypeRef      = []
        CS_opArgument_TypeRef       = []

        ElementPackages , ElementPackagesID = self.getElementPackages()

        if Tag.inputTypeReference in ElementPackages:
            TypeRefs.extend(ElementPackages[Tag.inputTypeReference])

            for Item in ElementPackagesID[Tag.inputSenderRecieverInterface]:
                if TypeRefs != []:
                    if type(TypeRefs[0]) == str:
                        SR_dataElement_TypeRef.append(TypeRefs.pop(0))
            
            for Item in ElementPackagesID[Tag.inputClientServerInterface]:
                if TypeRefs != []:
                    if type(TypeRefs[0]) == str:
                        CS_opArgument_TypeRef.append(TypeRefs.pop(0))
            
            ImplementationDataTypeIDs = ElementParser(self.arxmlInputFilePath).getImplementationTypesID()

            for Item in SR_dataElement_TypeRef:
                if type(Item) == str:
                    for IDname in ImplementationDataTypeIDs:
                        if Item.split('/')[-1] == IDname:
                            SR_dataElement_TypeRefID.append(ImplementationDataTypeIDs[IDname])
            
            for Item in CS_opArgument_TypeRef:
                if type(Item) == str:
                    for IDname in ImplementationDataTypeIDs:
                        if Item.split('/')[-1] == IDname:
                            CS_opArgument_TypeRefID.append(ImplementationDataTypeIDs[IDname])
        
        return SR_dataElement_TypeRefID,CS_opArgument_TypeRefID
            

    def getSenderRecieverInterfaces(self):
        
        SenderRecieverInterfaces            = []
        SenderRecieverInterfacesID          = {}
        
        SR_dataElement_TypeRefID            = self.getTypeRefID()[0]
        SR_dataElements                     = []

        ElementPackages,ElementPackagesID   = self.getElementPackages()

        for item in ElementPackages[Tag.inputSenderRecieverInterface]:
            
            numberOfDataElements    =   range(1)    # should loop on the number of dataElements in the interface must be configued

            for DEnameIndex in numberOfDataElements:     
                SR_dataElements.append(DataElement(ElementPackages[Tag.inputSRDataElement].pop(0),SR_dataElement_TypeRefID.pop(0)))
                    
            SenderRecieverInterfaces.append(SenderRecieverInterface(item,SR_dataElements))
            
            SR_dataElements.clear() 

        for ID in ElementPackagesID[Tag.inputSenderRecieverInterface]:
            SenderRecieverInterfacesID[SenderRecieverInterfaces[ID].Name]   =   ID
        
        return SenderRecieverInterfaces,SenderRecieverInterfacesID

    
    def getClientServerInterfaces(self):

        ClientServerInterfaces      = []
        ClientServerInterfacesID    = {}  

        CS_opArgument_TypeRefID   = self.getTypeRefID()[1]
        CS_operations             = []

        ElementPackages,ElementPackagesID   = self.getElementPackages()

        for item in ElementPackages[Tag.inputClientServerInterface]:

            numberOfOperation   =   range(1)    # should loop on the number of operaions in the interface must be configue

            for CSoperation in numberOfOperation:
                CS_operations.append(Operation(ElementPackages[Tag.inputCSOperation].pop(0)))

                for Argument in range(1):   # should loop on the number of arguments in the operation must be configued
                    CS_operations[-1].addArgument(ElementPackages[Tag.inputOpArgument].pop(0),
                                                        CS_opArgument_TypeRefID.pop(0),ElementPackages[Tag.inputOpArgumentDirection].pop(0))
                    
                #ErrorRefs should be configured

            ClientServerInterfaces.append(ClientServerInterface(item,CS_operations))
            CS_operations.clear()
        
        for ID in ElementPackagesID[Tag.inputClientServerInterface]:
            ClientServerInterfacesID[ClientServerInterfaces[ID].Name]   =   ID

        return ClientServerInterfaces,ClientServerInterfacesID





#x,y=InterfaceParser('DataTypesAndInterfaces.arxml').getClientServerInterfaces()
"""
print(x[Tag.inputSRDataElement])
x[Tag.inputSRDataElement].pop(0)
print(x[Tag.inputSRDataElement])
"""
"""for i in x:
    print(i.Name , y[x.index(i)])
    for e in i.Operations:
        print(e.Name)
        for s in e.Arguments:
            print(s.Name,e.ArgumentsDirection[e.Arguments.index(s)])
"""
#print(x[0].Name,x[0].Data_Elements)