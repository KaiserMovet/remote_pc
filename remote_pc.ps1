cd $(split-path -parent $MyInvocation.MyCommand.Definition)
python3 -m virtualenv env
python3 remote_pc.py
timeout 20
