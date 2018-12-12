@echo off

set "pyQtScriptsPath=C:\Users\sesa236189\AppData\Local\Programs\Python\Python37\Scripts"
set "qtGuiPath=C:\Users\sesa236189\OneDrive - Schneider Electric\Documents\Perso\pop-it\Projects\Zuora\ZTool_clean\ZTool_clean\BillingPreview\UI\qt"
set "pyGuiPath=C:\Users\sesa236189\OneDrive - Schneider Electric\Documents\Perso\pop-it\Projects\Zuora\ZTool_clean\ZTool_clean\BillingPreview\UI"
set "qtUiName=ZTools.ui"
set "pyUiName=ZToolsUi.py"
set "qtRCName=ZTools.qrc"
set "pyRCName=ztools_rc.py"

echo "python resources generation"
"%pyQtScriptsPath%\pyrcc5.exe" "%qtGuiPath%\%qtRCName%" -o "%pyGuiPath%\%pyRCName%"