
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
    inputImplementationType          = 'IMPLEMENTATION-DATA-TYPE'
    inputImplementationTypeElement   = 'IMPLEMENTATION-DATA-TYPE-ELEMENT'
    inputTypeCategory                = 'CATEGORY'
    inputArraySize                   = 'ARRAY-SIZE'
    inputArraySizeSemantics          = 'ARRAY-SIZE-SEMANTICS'
    inputImplementationTypeReference = 'IMPLEMENTATION-DATA-TYPE-REF'
    inputSWbaseTypes                 = 'SW-BASE-TYPE'
    inputBaseTypeSize                = 'BASE-TYPE-SIZE'
    inputBaseTypeReference           = 'BASE-TYPE-REF'

    inputSenderRecieverInterface     = 'SENDER-RECEIVER-INTERFACE'
    inputSRDataElement               = 'VARIABLE-DATA-PROTOTYPE'
    inputTypeReference               = 'TYPE-TREF'
    inputClientServerInterface       = 'CLIENT-SERVER-INTERFACE'
    inputCSOperation                 = 'CLIENT-SERVER-OPERATION'
    inputOpArgument                  = 'ARGUMENT-DATA-PROTOTYPE'
    inputOpArgumentDirection         = 'DIRECTION'
    inputPossibleErrorRef            = 'POSSIBLE-ERROR-REFS'
    inputPossibleError               = 'POSSIBLE-ERRORS'
    
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
