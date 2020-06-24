import sys
sys.path.append('../')
# Description : This Class contains only all arxml common needed tags of the AUTOSAR Schema.

class Tag:

    AUTOSAR_Schema  = None #Holds the namespace of the AUTOSAR schema

    inputParameters                  = 'PARAMETERS'
    inputReferences                  = 'REFERENCES'
    inputSubContainer                = 'SUB-CONTAINERS'
    inputContainer                   = 'CONTAINERS'
    inputModule                      = 'Module'
    inputShortName                   = 'SHORT-NAME'
    inputDescription                 = 'DESC'
    generationValue                  = 'VALUE'
    inputLowerMultiplicity           = 'LOWER-MULTIPLICITY'
    inputUpperMultiplicity           = 'UPPER-MULTIPLICITY'
    inputUpperMultiplicityInfinity   = 'UPPER-MULTIPLICITY-INFINITE'
    inputEnumLiterals                = 'ECUC-ENUMERATION-LITERAL-DEF'
    inputReferenceDestRef            = 'DESTINATION-REF'

    '''Data Types packages Tags'''
    inputImplementationType          = 'IMPLEMENTATION-DATA-TYPE'
    inputImplementationTypeElement   = 'IMPLEMENTATION-DATA-TYPE-ELEMENT'
    inputTypeCategory                = 'CATEGORY'
    inputArraySize                   = 'ARRAY-SIZE'
    inputArraySizeSemantics          = 'ARRAY-SIZE-SEMANTICS'
    inputImplementationTypeReference = 'IMPLEMENTATION-DATA-TYPE-REF'
    inputSWbaseTypes                 = 'SW-BASE-TYPE'
    inputBaseTypeSize                = 'BASE-TYPE-SIZE'
    inputBaseTypeReference           = 'BASE-TYPE-REF'
    inputSubElements                 = 'SUB-ELEMENTS'
    inputDataTypeRef                 = 'SW-DATA-DEF-PROPS-CONDITIONAL'
    '''Interfacing packages Tags'''
    inputSenderRecieverInterface     = 'SENDER-RECEIVER-INTERFACE'
    inputSRDataElement               = 'VARIABLE-DATA-PROTOTYPE'
    inputTypeReference               = 'TYPE-TREF'
    inputClientServerInterface       = 'CLIENT-SERVER-INTERFACE'
    inputOperation                   = 'OPERATIONS'
    inputCSOperation                 = 'CLIENT-SERVER-OPERATION'
    inputArguments                   = 'ARGUMENTS'
    inputOpArgument                  = 'ARGUMENT-DATA-PROTOTYPE'
    inputOpArgumentDirection         = 'DIRECTION'
    inputPossibleErrorRef            = 'POSSIBLE-ERROR-REFS'
    inputPossibleError               = 'POSSIBLE-ERRORS'
    '''Application software components Tags'''
    inputApplicationSWC              = 'APPLICATION-SW-COMPONENT-TYPE'
    inputRequiredPortPrototype       = 'R-PORT-PROTOTYPE'
    inputProviderPortPrototype       = 'P-PORT-PROTOTYPE'
    inputDataElementRef              = 'DATA-ELEMENT-REF'
    inputOperationRef                = 'OPERATION-REF'
    inputRequiredInterfaceRef        = 'REQUIRED-INTERFACE-TREF'
    inputProviderInterfaceRaf        = 'PROVIDED-INTERFACE-TREF'
    inputSWinternalBehaviour         = 'SWC-INTERNAL-BEHAVIOR'
    inputInitEvent                   = 'INIT-EVENT'
    inputOperationInvEvent           = 'OPERATION-INVOKED-EVENT'
    inputOnDataReception             = 'ON-DATA-RECEPTION-EVENT'
    inputTimingEvent                 = 'TIMING-EVENT'
    inputStartOnEventRef             = 'START-ON-EVENT-REF'
    inputContextProviderPortRef      = 'CONTEXT-P-PORT-REF'
    inputContextRequirePortRef       = 'CONTEXT-R-PORT-REF'
    inputTargetProvidedOpRef         = 'TARGET-PROVIDED-OPERATION-REF'
    inputTargetRequireDataRef        = 'TARGET-REQUIRE-DATAELEMENT-REF'
    inputEventPeriod                 = 'PERIOD'
    inputRunnableEntityName          = 'RUNNABLE-ENTITY'
    inputCanInvokedConcurrently      = 'CAN-BE-INVOKED-CONCURRENTLY'
    inputRunnableMinStartInterval    = 'MINIMUM-START-INTERVAL'
    inputRunnableSymbol              = 'SYMBOL'
    inputSWCimplementation           = 'SWC-IMPLEMENTATION'
    inputBehaviourRef                = 'BEHAVIOR-REF'


    
    '''output arxml common tags '''
    
    AUTOSAR="AUTOSAR"
    Packages="AR-PACKAGES"
    Package="AR-PACKAGE"
    Elements="ELEMENTS"
    ShortName="SHORT-NAME"
    ConfValues="ECUC-MODULE-CONFIGURATION-VALUES"
    Containers="CONTAINERS"
    DestinationRef = 'DESTINATION-REF'
    ConfContainerValue="ECUC-PARAM-CONF-CONTAINER"
    ChoiceContainerValue = "ECUC-CHOICE-CONTAINER"
    ParameterValues="PARAMETER-VALUES"
    NumericalValue="ECUC-INTEGER-PARAM-VALUE"
    FloatValue="ECUC-FLOAT-PARAM-VALUE"
    FunctionNameValue = "ECUC-FUNCTION-NAME-VALUE"
    StringValue="ECUC-STRING-PARAM-VALUE"
    BooleanValue="ECUC-BOOLEAN-PARAM-VALUE"
    EnumerartionValue="ECUC-ENUMERATION-PARAM-VALUE"
    Value="VALUE"
    RefernceValue = 'REFERENCE-VALUES'
    RefInfoTag = 'ECUC-REFERENCE'
    DestinationRef = 'DESTINATION-REF'
    SubContainer="SUB-CONTAINERS"
    Choices = "CHOICES"


    def __init__(self, schemaVersion):

        self.AUTOSAR_Schema = schemaVersion
