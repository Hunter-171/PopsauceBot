# NOTICE
### Development on PopsauceBot has been paused temporarily
We regret to inform you that the development of PopsauceBot is currently on hold. This decision comes as a result of recent changes to the web environment that have been made by JKLM, this package no longer works as it fails to connect to the sockets properly without the ReCaptcha token. 

I cannot confirm that I will return to PopsauceBot due to other projects needing my attention, but I remain hopeful about its future development. I encourage and welcome pull requests, each submitted pull request will be reviewed and if deemed good enough will be merged.

# PopsauceBot
Library for popsauce @ jklm.fun.

### This repository is for educational purposes only.

Answers will be updated every 1-2 weeks

## Usage

```python
from popbot import *

def handleChat(sender, message, ws):
    PopsauceClient.handleChat(sender, message) # You get the sender, message and websocket

def handleAnswer(answer, ws):
    PopsauceClient.instantType(answer, ws)     # You get the answer and the websocket

def playGame():
    client = PopsauceClient("Ken Miles", "DMJM", handleChat, handleAnswer)  # username, roomCode
    client.joinRoom()                      # Join room
    client.sendChat("Bruh")                # Send message in chat
    client.joinRound()                     # Joins the round
    client.playRound()                     # Plays for your (answers)

playGame()
```

## Quick Start
Running `launcher.py` will allow you to play the game from the console.

## Videos
[Example 1](https://www.youtube.com/watch?v=lXkM882SYpU)
Javascript version that shows the answers for you when the question is clicked.

## Project Ideas
- ChatBot
