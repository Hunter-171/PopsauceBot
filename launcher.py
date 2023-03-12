from popbot import PopsauceClient

if __name__ == "__main__":
    client = PopsauceClient("Mr.nobody", "PBKZ")
    client.joinRoom()

    while True:
        # Get user input for command
        print("For commands, type help")
        Input = input(" ")
        
        if Input == "play":
            # Play a round
            client.playRound()
            
        elif Input == "help":
            # Display commands and help
            print("play -- Play a round of Popsauce")
            print("join -- Join a room of Popsauce")
            print("message -- After type in message when promted to send in chat")
            
        elif Input == "join":
            # Join room
            client.joinRound()
            
        elif Input == "message":
            msg = input("Enter message to send: ")
            client.sendChat(msg)
        
        else:
            print("'"+Input+"' is not a recognized command.")
