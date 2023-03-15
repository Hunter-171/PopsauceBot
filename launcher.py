from popbot import PopsauceClient
from threading import Thread

def handleChat(client, sender, message):
    PopsauceClient.handleChat(client, sender, message)

def handleAnswer(answer, ws):
    print()

if __name__ == "__main__":
    client = PopsauceClient(input("Username: "), input("Room Code: "), handleChat, handleAnswer)
    client.joinRoom()

    print()
    print("Do \"/join\" to join the game!")
    print("Do \"/play\" to start playing!")
    print("Do \"/answer\" to answer!")
    print()

    playing = False

    def playRound(client):
        global playing
        if playing:
            print("Already playing...")
            return
        print("Started playing...")
        playing = True
        client.playRound()
        print("Finished playing...")
        playing = False

    def play(client):
        th = Thread(target=playRound, args=[client])
        th.start()

    while True:
        # Get user input for message to send
        message = input()

        if message.lower() == "/play":
            # Play a round
            play(client)
        elif message.lower() == "/join":
            # Join round
            print("Joined round")
            client.joinRound()
        elif message.lower().split(" ")[0] == "/answer":
            # Answer With User Input
            client.instantType(message.split(" ",1)[1], client.gameSocket)
        else:
            # Send chat message
            print(message.lower().split(" ")[0])
            client.sendChat(message)
            
