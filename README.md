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
