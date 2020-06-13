import sys
sys.path.append('../Module')
sys.path.append('../Container')
sys.path.append('../Parameter')
sys.path.append('../Reference')
sys.path.append('../ContainerList')

#===============================================================
from Module import Module
from Container import Container
from ContainerList import ContainerList
from parameter 	import Parameter
from Reference import Reference


modulesList=[] #SoAd  NVM  CAN

containerListOfLists=[] #SoAdConfig SoAdGeneral

SubcontainerListOfLists=[]

#SoAdConfig  ContainerList
#instance
parameterList_SoAdConfig_0=[]
referenceList_SoAdConfig_0=[]
#instance
parameterList_SoAdConfig_1=[]
referenceList_SoAdConfig_1=[]


parameter_SoAdConfig_0_DevErrorDetect= Parameter(shortName="DevErrorDetect",value="1")
parameter_SoAdConfig_1_DevErrorDetect= Parameter(shortName="DevErrorDetect",value="0")

parameterList_SoAdConfig_0.append(parameter_SoAdConfig_0_DevErrorDetect)
parameterList_SoAdConfig_1.append(parameter_SoAdConfig_1_DevErrorDetect)

reference_SoAdConfig_0_SocketConnectionRef= Reference(shortName="SocketConnectionRef_0")
reference_SoAdConfig_1_SocketConnectionRef= Reference(shortName="SocketConnectionRef_1")

referenceList_SoAdConfig_0.append(reference_SoAdConfig_0_SocketConnectionRef)
referenceList_SoAdConfig_1.append(reference_SoAdConfig_1_SocketConnectionRef)

subContainer_SoAdBSW_0=Container("SoAdBSW_0")
subContainer_SoAdBSW_1=Container("SoAdBSW_1")
subContainer_SoAdConfig_0_SoAdBSW=ContainerList("SoAdBSW",[subContainer_SoAdBSW_0,subContainer_SoAdBSW_1])

SubcontainerListOfLists.append(subContainer_SoAdConfig_0_SoAdBSW)

container_SoAdConfig_0=Container("SoAdConfig_0",subContainers=SubcontainerListOfLists,parameters=parameterList_SoAdConfig_0,references=referenceList_SoAdConfig_0)
container_SoAdConfig_1=Container("SoAdConfig_1",parameters=parameterList_SoAdConfig_1,references=referenceList_SoAdConfig_1)
container_SoAdGeneral_0=Container("SoAdGeneral_0")


#print(container_SoAdConfig_0.parameters[0].shortName,container_SoAdConfig_0.parameters[0].value)
#print(container_SoAdConfig_1.parameters[0].value)
#print(container_SoAdGeneral_0.parameters[0].value)

container_SoAdConfig=ContainerList("SoAdConfig",[container_SoAdConfig_0,container_SoAdConfig_1])
container_SoAdGeneral=ContainerList("SoAdGeneral",[container_SoAdGeneral_0])


containerListOfLists.append(container_SoAdConfig)
containerListOfLists.append(container_SoAdGeneral)



SoAd=Module("SoAd","XXX","1",containerListOfLists)
modulesList.append(SoAd)

#print(SoAd.containers[0].listOfContainerInstances[0].subContainers[0].listOfContainerInstances[0].shortName)

#===============================================================
	# temp_mod_1=Module()
	# temp_mod_2=Module()
	# user_mod_1=Module()
	# user_mod_2=Module()
	
	# template = [temp_mod_1,temp_mod_2]
	# data	   = [user_mod_1,user_mod_2]
	
	# 			modules SoAd    module SoAd
	# 			mult  3

	# 			SoAd                   SoAd	  					
	# 				sub_1                SoAd_0
	# 				sub_2					sub_1 sub_2
	# 									 SoAd_1
	# 									 	sub_1 sub_2
#===============================================================	