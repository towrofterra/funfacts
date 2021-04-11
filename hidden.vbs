Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c copy_fun_fact_to_clipboard.bat"
oShell.Run strArgs, 0, false
