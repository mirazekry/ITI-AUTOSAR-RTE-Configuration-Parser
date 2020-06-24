import sys
sys.path.append('../')

from InputPathes.Tag                           import Tag
from InputPathes.InputPathes                   import Inputs
from ApplicationSWC.Ports                      import Port
from ApplicationSWC.Events                     import *
from ApplicationSWC.Runnables                  import Runnable
from Base.BaseParser                           import BaseParser
from Interfaces.InterfacesParser               import InterfaceParser
from ApplicationSWC.InternalBehavior           import InternalBehavior
from ApplicationSWC.Application_SWC_Type       import Application_SWC
from Interfaces.ClientServerInterface          import ClientServerInterface
from Interfaces.SenderRecieverInterface        import SenderRecieverInterface


# Description : This Class contains Application Software Component parsing

class ApplicationSWCparser(BaseParser):

    PackagesSource = [  Tag.inputInitEvent,
                        Tag.inputApplicationSWC,
                        Tag.inputRequiredPortPrototype,
                        Tag.inputProviderPortPrototype,
                        Tag.inputDataElementRef,
                        Tag.inputOperationRef,
                        Tag.inputRequiredInterfaceRef,
                        Tag.inputProviderInterfaceRaf,
                        Tag.inputSWinternalBehaviour,              
                        Tag.inputOperationInvEvent,
                        Tag.inputOnDataReception,
                        Tag.inputTimingEvent,
                        Tag.inputStartOnEventRef,
                        Tag.inputContextProviderPortRef,
                        Tag.inputContextRequirePortRef,
                        Tag.inputTargetProvidedOpRef,
                        Tag.inputTargetRequireDataRef,
                        Tag.inputEventPeriod,
                        Tag.inputRunnableEntityName,
                        Tag.inputCanInvokedConcurrently,
                        Tag.inputRunnableMinStartInterval,
                        Tag.inputRunnableSymbol,
                        Tag.inputSWCimplementation,
                        Tag.inputBehaviourRef   ]


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

    def getPorts(self):

        Ports   = []
        PortsID = {}

        ElementPackages = self.getElementPackages()[0]
        
        Interface   =   InterfaceParser(Inputs.DataTypesAndInterfaces_filePath)
        SR_ID       =   Interface.getSenderRecieverInterfaces()[1]
        CS_ID       =   Interface.getClientServerInterfaces()[1]
        
        '''Require Port'''
        if Tag.inputRequiredPortPrototype in ElementPackages:
            for item in ElementPackages[Tag.inputRequiredPortPrototype]:
                name        =   item
                portType    =   'R-Port'
                
                if Tag.inputRequiredInterfaceRef in ElementPackages:
            
                    if ElementPackages[Tag.inputRequiredInterfaceRef][0].split('/')[-1] in SR_ID :
                        InterfaceType = 'Sender_Reciever_Interface'
                        InterfaceID   = SR_ID[ElementPackages[Tag.inputRequiredInterfaceRef][0].split('/')[-1]]
                            
                        if Tag.inputDataElementRef in ElementPackages:
                            DataElement = ElementPackages[Tag.inputDataElementRef].pop(0).split('/')[-1]
                        else:
                            DataElement = None
                            
                        Ports.append(Port(name,portType,InterfaceType,InterfaceID))
                        Ports[-1].addDataElement(DataElement)
                        
                   
                    if ElementPackages[Tag.inputRequiredInterfaceRef][0].split('/')[-1] in CS_ID:
                        InterfaceType = 'Client_Server_Interface'
                        InterfaceID   = CS_ID[ElementPackages[Tag.inputRequiredInterfaceRef][0].split('/')[-1]]
                            
                        if Tag.inputOperationRef in ElementPackages:
                            Operation = ElementPackages[Tag.inputOperationRef].pop(0).split('/')[-1]
                        else:
                            Operation = None
                            
                        Ports.append(Port(name,portType,InterfaceType,InterfaceID))
                        Ports[-1].addOperation(Operation)
                            

                    ElementPackages[Tag.inputRequiredInterfaceRef].pop(0)
            
        
        '''Provider Port'''
        if Tag.inputProviderPortPrototype in ElementPackages:
            for item in ElementPackages[Tag.inputProviderPortPrototype]:
                name        =   item
                portType    =   'P-Port'
                
                if Tag.inputProviderInterfaceRaf in ElementPackages:
                    if ElementPackages[Tag.inputProviderInterfaceRaf][0].split('/')[-1] in SR_ID :
                        InterfaceType = 'Sender_Reciever_Interface'
                        InterfaceID   =  SR_ID[ElementPackages[Tag.inputProviderInterfaceRaf][0].split('/')[-1]]
                            
                        if Tag.inputDataElementRef in ElementPackages:
                            DataElement = ElementPackages[Tag.inputDataElementRef].pop(0).split('/')[-1]
                        else:
                            DataElement = None
                            
                        Ports.append(Port(name,portType,InterfaceType,InterfaceID))
                        Ports[-1].addDataElement(DataElement)
 
                    
                    if ElementPackages[Tag.inputProviderInterfaceRaf][0].split('/')[-1] in CS_ID:
                        InterfaceType = 'Client_Server_Interface'
                        InterfaceID   = CS_ID[ElementPackages[Tag.inputProviderInterfaceRaf][0].split('/')[-1]]

                        if Tag.inputOperationRef in ElementPackages:
                            Operation = ElementPackages[Tag.inputOperationRef].pop(0).split('/')[-1]
                        else:
                            Operation = None
                            
                        Ports.append(Port(name,portType,InterfaceType,InterfaceID))
                        Ports[-1].addOperation(Operation)
                            

                    ElementPackages[Tag.inputProviderInterfaceRaf].pop(0)


        for port in Ports:
            PortsID[port.Name]  =   Ports.index(port)
        
        return Ports,PortsID


    def getRunnables(self):
        
        Runnables       = []
        RunnablesID     = {}
        ElementPackages,ElementPackagesID = self.getElementPackages()

        if Tag.inputRunnableEntityName in ElementPackagesID:
            for RunnableID in ElementPackagesID[Tag.inputRunnableEntityName]:
                Name                = ElementPackages[Tag.inputRunnableEntityName][RunnableID]
                CanBeInvokedState   = ElementPackages[Tag.inputCanInvokedConcurrently][RunnableID]
                MinStartInterval    = ElementPackages[Tag.inputRunnableMinStartInterval][RunnableID]
                Symbol              = ElementPackages[Tag.inputRunnableSymbol][RunnableID]
                
                RunnablesID[Name]   =   RunnableID

                Runnables.append(Runnable(Name,CanBeInvokedState,MinStartInterval,Symbol))

        return Runnables,RunnablesID


    def getEvents(self):

        InitEvent_List                  =   []
        TimingEvent_List                =   []
        OnDataReceptionEvent_List       =   []
        OnOperationInvokedEvent_List    =   []

        Runnables_list                  =   self.getRunnables()[1]
        Ports_List                      =   self.getPorts()[1]

        ElementPackages,ElementPackagesID   =   self.getElementPackages()

        if Tag.inputInitEvent in ElementPackages:
            
            for ID in ElementPackagesID[Tag.inputInitEvent]:
                Name = ElementPackages[Tag.inputInitEvent][ID]
               
                RunnableEntityID    =   Runnables_list[ElementPackages[Tag.inputStartOnEventRef][0].split('/')[-1]]
                ElementPackages[Tag.inputStartOnEventRef].pop(0)
                        
                InitEvent_List.append(InitEvent(Name,RunnableEntityID))

        if Tag.inputOperationInvEvent in ElementPackages:

            for ID in ElementPackagesID[Tag.inputOperationInvEvent]:
                Name = ElementPackages[Tag.inputOperationInvEvent][ID]
                
                RunnableEntityID    =   Runnables_list[ElementPackages[Tag.inputStartOnEventRef][0].split('/')[-1]]
                ElementPackages[Tag.inputStartOnEventRef].pop(0)
                
                PortID              =   Ports_List[ElementPackages[Tag.inputContextProviderPortRef][ID].split('/')[-1]]

                operation           =   ElementPackages[Tag.inputTargetProvidedOpRef][ID].split('/')[-1]

                OnOperationInvokedEvent_List.append(OnOperationInvoked(Name,RunnableEntityID,PortID,operation))
        

        if Tag.inputOnDataReception in ElementPackages:

            for ID in ElementPackagesID[Tag.inputOnDataReception]:
                Name = ElementPackages[Tag.inputOnDataReception][ID]

                RunnableEntityID    =   Runnables_list[ElementPackages[Tag.inputStartOnEventRef][0].split('/')[-1]]
                ElementPackages[Tag.inputStartOnEventRef].pop(0)

                PortID              =   Ports_List[ElementPackages[Tag.inputContextRequirePortRef][ID].split('/')[-1]]

                DataElement         =   ElementPackages[Tag.inputContextRequirePortRef][ID].split('/')[-1]

                OnDataReceptionEvent_List.append(OnDataReceptionEvent(Name,RunnableEntityID,PortID,DataElement))

        if  Tag.inputTimingEvent in ElementPackages:

            for ID in ElementPackagesID[Tag.inputTimingEvent]:
                Name = ElementPackages[Tag.inputTimingEvent][ID]

                RunnableEntityID    =   Runnables_list[ElementPackages[Tag.inputStartOnEventRef][0].split('/')[-1]]
                ElementPackages[Tag.inputStartOnEventRef].pop(0)

                periodicity         =   ElementPackages[Tag.inputEventPeriod][ID]

                TimingEvent_List.append(TimingEvent(Name,RunnableEntityID,periodicity))

        return  InitEvent_List,TimingEvent_List,OnDataReceptionEvent_List,OnOperationInvokedEvent_List
            

    def getInternalBehavior(self):

        InternalBehavior_List = []

        ElementPackages             =   self.getElementPackages()[0]
        SWC_InternalBehavior_Name   =   ElementPackages[Tag.inputSWinternalBehaviour][0]

        I_Event, T_Event, ODR_Event, OPI_Event = self.getEvents()

        Runnables_list  =   self.getRunnables()[0]

        InternalBehavior_List.append(InternalBehavior(SWC_InternalBehavior_Name,I_Event,T_Event,ODR_Event,OPI_Event,Runnables_list)) 

        return InternalBehavior_List


    def getApplicationSWC(self):

        Application_SWC_List    =   []

        SWC_Name                =   self.getElementPackages()[0][Tag.inputApplicationSWC]

        Application_SWC_List.append(Application_SWC(SWC_Name,self.getPorts()[0],self.getInternalBehavior()))

        return Application_SWC_List





"""x=ApplicationSWCparser('First_SWC.arxml')
for i in x.getApplicationSWC():
    print (i.Name)
    for j in i.Ports:
        print(j.Name)
    for j in i.InternalBehavoirs:
        print(j.Name)
"""
                    

"""
x=ApplicationSWCparser('SWC2.arxml')
for i in x.getPorts():
    print (i.Name)


x=ApplicationSWCparser('SWC3.arxml')
for i in x.getPorts():
    print (i.Name)

"""













