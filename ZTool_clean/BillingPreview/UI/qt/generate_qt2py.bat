@echo off

set "pyQtScriptsPath=C:\Users\sesa236189\AppData\Local\Programs\Python\Python37\Scripts"
set "qtGuiPath=C:\Users\sesa236189\OneDrive - Schneider Electric\Documents\Perso\pop-it\Projects\Zuora\ZTool_clean\ZTool_clean\BillingPreview\UI\qt"
set "pyGuiPath=C:\Users\sesa236189\OneDrive - Schneider Electric\Documents\Perso\pop-it\Projects\Zuora\ZTool_clean\ZTool_clean\BillingPreview\UI"
set "qtUiName=ZTools.ui"
set "pyUiName=ZTools.py"
set "qtRCName=ZTools.qrc"
set "pyRCName=ZTools_rc.py"

echo "python UI generation"
"%pyQtScriptsPath%\pyuic5.exe" -x "%qtGuiPath%\%qtUiName%" -o "%pyGuiPath%\%pyUiName%"
echo "python resources generation"
"%pyQtScriptsPath%\pyrcc5.exe" "%qtGuiPath%\%qtRCName%" -o "%pyGuiPath%\%pyRCName%"