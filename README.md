# PopsauceBot
Library for popsauce @ jklm.fun.

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
