if ((Test-Path "env") -eq 0) {
    python3 -m pip install virtualenv
    python3 -m virtualenv env
    ./env/Scripts/activate.ps1
    python3 -m pip install -r requirements
}
$Source = $(get-location).Path + "\remote_pc.ps1"
$Target = "$HOME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\remote_pc.lnk"
$WshShell = New-Object -comObject WScript.Shell
New-Item -ItemType SymbolicLink -Path $Target -Target $Source