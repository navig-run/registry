' run-hidden.vbs  --  launch the devtools engine with NO window at all.
'
' Explorer fires a "%1" verb once per selected file; "powershell -WindowStyle
' Hidden" still flashes a console each time ("dozens of windows"). wscript has
' no console of its own and Run(..., 0, False) starts the child hidden, so the
' per-file collectors are truly windowless -- only the single coalesced worker
' window (spawned by the engine) is shown.
'
' Usage: wscript run-hidden.vbs <interpreter> <devtools.ps1> <command> <target>

Option Explicit
Dim a, line
Set a = WScript.Arguments
If a.Count < 4 Then WScript.Quit 1
line = """" & a(0) & """ -NoProfile -ExecutionPolicy Bypass -File """ & a(1) & """ " & a(2) & " --target """ & a(3) & """"
CreateObject("WScript.Shell").Run line, 0, False
