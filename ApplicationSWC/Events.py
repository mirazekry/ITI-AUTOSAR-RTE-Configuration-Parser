import sys
sys.path.append('../')

from Base.BaseElement import BaseElement

class InitEvent(BaseElement):

    def __init__(self,Name = None, RunnableEntityID = None):

        super().__init__(Name)
        
        self.RunnableEntityID   =   RunnableEntityID



class TimingEvent(BaseElement):

    def __init__(self,Name = None,RunnableEntityID= None,Periodicity = None):

        super().__init__(Name)

        self.RunnableEntityID   =   RunnableEntityID

        self.Periodicity        =   Periodicity


class OnDataReceptionEvent(BaseElement):

    def __init__(self,Name = None,RunnableEntityID = None,PortID = None,DataElement = None):

        super().__init__(Name)

        self.RunnableEntityID   =   RunnableEntityID

        self.PortID             =   PortID

        self.DataElement        =   DataElement


class OnOperationInvoked(BaseElement):

    def __init__(self,Name = None,RunnableEntityID = None,PortID = None,Operation = None):

        super().__init__(Name)

        self.RunnableEntityID   =   RunnableEntityID

        self.PortID             =   PortID

        self.Operation          =   Operation