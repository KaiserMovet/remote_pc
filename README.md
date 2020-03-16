# Remote PC
The software is used to download commands via https from the server and then execute them.
The main purpose is to enable predefined commands via IFTTT and WebHook.

## Description
The software executes a request to the specified page every specified time.
If it receives a command, it will execute it.

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
