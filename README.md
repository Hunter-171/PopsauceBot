# PopsauceBot
Library for popsauce @ jklm.fun.

## Usage

```python
from popbot import *

def playGame():
    client = PopsauceClient("ken", "MHQX")
    client.joinRoom()
    client.sendChat("Bruh")
    client.playRound()

playGame()
```
