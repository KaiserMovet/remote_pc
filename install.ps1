#Creating virtual env
if ((Test-Path "env") -eq 0) {
    python3 -m pip install virtualenv
    python3 -m virtualenv env
    ./env/Scripts/activate.ps1
    python3 -m pip install -r requirements.txt
}
#Adding task to scheduler
$source = $(get-location).Path + "\remote_pc.ps1"
$file_content = Get-Content .\res\remote_pc.xml | out-string
$file_content = $file_content.replace("{{remote_pc_path}}", $source)
Register-ScheduledTask -Xml $file_content -TaskName "Remote_pc"