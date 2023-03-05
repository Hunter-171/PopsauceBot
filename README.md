# PopsauceBot
Library for popsauce @ jklm.fun.

### This repository is for educational purposes only.

Answers will be updated every 1-2 weeks

## Usage

```python
from popbot import *

def playGame():
    client = PopsauceClient("ken", "MHQX") # username, roomCode
    client.joinRoom()                      # Join room
    client.sendChat("Bruh")                # Send message in chat
    client.playRound()                     # Plays for your (answers)

playGame()
```

## Videos
[Example 1](https://www.youtube.com/watch?v=lXkM882SYpU)
Javascript version that shows the answers for you when the question is clicked.
