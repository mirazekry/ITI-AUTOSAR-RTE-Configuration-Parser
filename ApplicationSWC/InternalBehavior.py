import sys
sys.path.append('../')

from Base.BaseElement import BaseElement

# Description : This Class contains Internal Behaviors lists

class InternalBehavior(BaseElement):

    def __init__(self,Name = None,InitEvents_List = [],TimingEvent_List = [],OnDataReceptionEvent_List = [],OnOperationInvoked_List = [],Runnables = [] ):

        super().__init__(Name)

        self.InitEvents_List             =   []
        self.TimingEvent_List            =   []
        self.OnDataReceptionEvent_List   =   []
        self.OnOperationInvoked_List     =   []

        self.Runnables                   =   []
        
        self.InitEvents_List.extend(InitEvents_List)
        self.TimingEvent_List.extend(TimingEvent_List)
        self.OnDataReceptionEvent_List.extend(OnDataReceptionEvent_List)
        self.OnOperationInvoked_List.extend(OnOperationInvoked_List)
        
        self.Runnables.extend(Runnables)