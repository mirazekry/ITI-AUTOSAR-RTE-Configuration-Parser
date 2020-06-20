from BaseType                import BaseType
from Operation               import Operation
from DataElement             import DataElement
from ImplementationDataType  import ImplementationDataType
from SenderRecieverInterface import SenderRecieverInterface
from ClientServerInterface   import ClientServerInterface
from ElementsParser          import ElementParser
from InterfacesParser        import InterfaceParser

## Description : This class contains all the application ports, interfaces, BaseTypes and SWCs

class Element:
    
    # Elements class contains all parameter's related info
    # Holds the AR-Package ShortName
    Package_Name           = None  
    
    # Elements Class constructor function
    def __init__(self):
        self.Package_Name    = ElementParser('DataTypesAndInterfaces.arxml').getARpackage()
        ## Application Elements Lists`
        self.Base_Data_Types                 = []
        self.Implementation_Data_Types       = []
        self.Sender_Reciever_Port_Interfaces = []
        self.Client_Server_Port_Interfaces   = []
        self.Application_SWC_Type            = []

    # Get Implementation Info
    def getBaseDataTypes(self):
        self.Base_Data_Types.extend(ElementParser('DataTypesAndInterfaces.arxml').parseBaseTypes())
            
    # Get Implementation Info
    def getImplementationDataTypes(self):
        self.Implementation_Data_Types.extend(ElementParser('DataTypesAndInterfaces.arxml').parseImplementationTypes())
    
    # Get Send Reciever Port Interface
    def getSenderRecieverPortIF(self):
        self.Sender_Reciever_Port_Interfaces.extend(InterfaceParser('DataTypesAndInterfaces.arxml').getSenderRecieverInterfaces()[0])

    # Get Client Server Port Interface
    def getClientServerPortIF(self):
        self.Client_Server_Port_Interfaces.extend(InterfaceParser('DataTypesAndInterfaces.arxml').getClientServerInterfaces()[0])
    
    
    
    

   

"""x=Element()
x.getBaseDataTypes()
x.getImplementationDataTypes()
x.getSenderRecieverPortIF()
x.getClientServerPortIF()

for i in x.Client_Server_Port_Interfaces:
    print(i.Name)
    for w in i.Operations:
        print(w.Name)
        for s  in w.ArgumentsDirection:
            print(s,"\n")

"""