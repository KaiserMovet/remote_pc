# Remote PC
The software is used to download commands via https from the server and then execute them.
The main purpose is to enable predefined commands via IFTTT and WebHook.

## Description
The software executes a request to the specified page every specified time.
If it receives a command, it will execute it.

- install.ps1 - script, which create python virtual env and add rempte_pc1 to task scheduler
- remote_pc.ps1 - script, wchich activate virtual env and run python script

Any custom commands can be added to `bin.command_executor.CommandExecutor`,
to dictionary `self.actions -> (Dict[command, function])`. 

## Instalation
1. Clone this repository
2. Run install.ps1 script in powershell as admin

## The supported commands are:
- computer shutdown ("turn_off")
- blocking          ("lock")
- Log off           ("logout")
- screen shutdown   ("screen_off")

## Prerequisite
- Windows
- Python 3.x

## Config file
- url - url to server
- interval [int] - interval beetween requests in seconds
