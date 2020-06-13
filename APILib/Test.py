
from ModuleClass import Module

SoAd = Module("SoAd",headerFilesPath='GeneratedFiles/',sourceFilesPath='GeneratedFiles/')
SoAd_CFG_H_Obj,SoAd_LCFG_H_Obj,SoAd_LCFG_C_Obj=SoAd.getFileObjects()


SoAd_CFG_H_Obj.writeNewLine(numberLines=4)
SoAd_CFG_H_Obj.writeCommentLine(comment="Hello \n There")
SoAd_CFG_H_Obj.writeNewLine()
SoAd_CFG_H_Obj.writeCommentMulLine(comment="Hello\nThere\nHello")
SoAd_CFG_H_Obj.writeNewLine(numberLines=8)
SoAd_CFG_H_Obj.writeCommentMulLine(comment="Pre Compile\nConfigurations",section=True)
SoAd_CFG_H_Obj.writeNewLine()
SoAd_CFG_H_Obj.createMacro("SoAd.SoAdConfig.SoAdConfig_0.DevErrorDetect","DEV_ERROR_DETECT",5)


SoAd_LCFG_H_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_H_Obj.writeCommentLine(comment="Hello \n There")
SoAd_LCFG_H_Obj.writeNewLine()
SoAd_LCFG_H_Obj.writeCommentMulLine(comment="Hello\nThere\nHello")
SoAd_LCFG_H_Obj.writeNewLine(numberLines=8)
SoAd_LCFG_H_Obj.writeCommentMulLine(comment="Pre Compile\nConfigurations",section=True)
SoAd_LCFG_H_Obj.writeNewLine()
SoAd_LCFG_H_Obj.createMacroStructLength("SoAd.SoAdConfig",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=2)
SoAd_LCFG_H_Obj.createMacroStructLength("SoAd.SoAdConfig.SoAdConfig_0.SoAdBSW",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=2)
SoAd_LCFG_H_Obj.createMacroStructLength("SoAd.SoAdGeneral",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_H_Obj.createMacroStructIndex("SoAd.SoAdConfig",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=2)
SoAd_LCFG_H_Obj.createMacroStructIndex("SoAd.SoAdConfig.SoAdConfig_0.SoAdBSW",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=2)
SoAd_LCFG_H_Obj.createMacroStructIndex("SoAd.SoAdGeneral",numberTabs=5)
SoAd_LCFG_H_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_H_Obj.createMacro("SoAd.SoAdConfig.SoAdConfig_0.DevErrorDetect",numberTabs=5)


SoAd_LCFG_C_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_C_Obj.writeCommentLine(comment="Hello \n There")
SoAd_LCFG_C_Obj.writeNewLine()
SoAd_LCFG_C_Obj.writeCommentMulLine(comment="Hello\nThere\nHello")
SoAd_LCFG_C_Obj.writeNewLine(numberLines=8)
SoAd_LCFG_C_Obj.writeCommentMulLine(comment="Pre Compile\nConfigurations",section=True)
SoAd_LCFG_C_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_C_Obj.createStruct("SoAd.SoAdConfig")
SoAd_LCFG_C_Obj.writeNewLine(numberLines=4)
SoAd_LCFG_C_Obj.createStruct("SoAd.SoAdGeneral")



SoAd.close()