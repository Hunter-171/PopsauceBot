from popbot import PopsauceClient
from time import sleep
def get_user_input():
    return input("Enter message to send: ")

if __name__ == "__main__":
    client = PopsauceClient("Mr.nobody", "PBKZ")
    client.joinRoom()

    while True:
        # Get user input for message to send
        message = get_user_input()

        if message == "play":
            # Play a round
            client.playRound()
        elif message == "join":
            # Join room
            client.joinRound()
        else:
            # Send chat message
            client.sendChat(message)
            
