import requests, string, random, names, hashlib, json, time, math
from websocket import WebSocket
from threading import Thread

def sha1(text):
    sha1 = hashlib.sha1()
    if(isinstance(text, (bytes, bytearray))):
        sha1.update(text)
    else:
        sha1.update(text.encode("utf-8"))
    return sha1.hexdigest()

def getWebSocketUrl(roomCode):
    r = requests.post("https://jklm.fun/api/joinRoom",json={"roomCode":roomCode})
    if("url" not in r.json()):
        print("❌ > Invalid room code")
        raise InvalidRoomCode()
    return r.json()["url"].split("//")[1]

def legitType(word, ws):
    out = ""
    time.sleep(0.6+max(random.random(),0.6)/2)
    for char in word:
        out += char
        if(len(out) % math.ceil(len(word)/4) != 0):continue
        sendRecv(ws, '42["submitGuess","'+out+'"]')
        time.sleep(max(random.random(),0.5)/5)
    time.sleep(0.6+max(random.random(),0.6)/3)
    sendRecv(ws, '42["submitGuess","'+out+'"]')

def sendRecv(ws, data):
    ws.send(data)
    return ws.recv()

def parse(text):
    try: return json.loads(text)
    except: return False

def lookupAnswer(challengeHash):
    with open("answers.txt","r",encoding="utf-8") as txt:
        for line in txt.read().split("\n"):
            challenge = line.split(":")
            if(len(challenge) > 1 and challenge[0] == challengeHash):
                return challenge[1]
    return None

def cacheAnswer(challengeHash, answer):
    with open("answers.txt","a",encoding="utf-8") as txt:
        txt.write(challengeHash+":"+answer+"\n")

class InvalidRoomCode(Exception):
    pass

class BannedFromRoom(Exception):
    pass

class PopsauceClient:
    def __init__(self, username, roomCode):
        self.username = username
        self.roomCode = roomCode
        self.userToken = "".join(random.choice(string.ascii_lowercase+"1234567890") for _ in range(16))
        self.chatSocket = WebSocket()
        self.gameSocket = WebSocket()
        self.url = getWebSocketUrl(roomCode)
        self.roomName = None
        self.peerId = None
        self.roomLanguage = None
        self.currentChallenge = None

    def sendChat(self, msg):
        self.chatSocket.send('42["chat","'+msg+'"]')

    def keepChatAlive(self):
        ws = self.chatSocket
        for _ in range(1000):
            msg = ws.recv()
            if(msg == "2"):
                ws.send("3")
                continue
            else:
                msgDict = parse("["+msg.split("[",1)[1])
                eventType = msgDict[0]
                if(eventType == "chat"):
                    sender = msgDict[1]["nickname"]
                    message = msgDict[2]
                    if(sender == self.username):continue
                    self.handleChat(sender, message)

    def handleChat(self, sender, message):
        print(f"<{sender}> " + message)

    def connectToChat(self):
        ws = self.chatSocket
        ws.connect("wss://"+self.url+"/socket.io/?EIO=4&transport=websocket")
        ws.recv()
        sendRecv(ws, "40")
        roomEntry = parse("["+sendRecv(ws, '420["joinRoom",{"roomCode":"'+self.roomCode+'","userToken":"'+self.userToken+'","nickname":"'+self.username+'","language":"en-US"}]').split("[",1)[1])
        if(len(roomEntry) == 2 and roomEntry[1] == "banned"):raise BannedFromRoom()
        self.peerId = roomEntry[0]["selfPeerId"]
        self.roomName = roomEntry[0]["roomEntry"]["name"]
        self.roomLanguage = roomEntry[0]["roomEntry"]["details"]
        Thread(target=self.keepChatAlive).start()

    def connectToGame(self):
        ws = self.gameSocket
        ws.connect("wss://"+self.url+"/socket.io/?EIO=4&transport=websocket")
        ws.recv()
        sendRecv(ws, "40")
        sendRecv(ws, '42["joinGame","popsauce","'+self.roomCode+'","'+self.userToken+'"]')

    def joinRound(self):
        sendRecv(self.gameSocket, '42["joinRound"]')

    def playRound(self):
        ws = self.gameSocket
        challengeHash = ""
        expectingImage = False
        for _ in range(1000):
            msg = ws.recv()
            if(str(len(msg)) == 0): continue
            elif(msg == "2"):
                ws.send("3")
                continue
            elif(msg == "41"):
                print("❌ > Disconnected")
                return
            else:
                if(isinstance(msg, (bytes, bytearray)) and expectingImage):
                    challengeHash = sha1(str(msg)+str(self.currentChallenge))
                    answer = lookupAnswer(challengeHash)
                    print("❔ > No Answer" if (answer == None) else "✔️  > " + answer)
                    if (answer != None):legitType(answer,ws)
                    continue
            msgDict = parse("["+msg.split("[",1)[1])
            eventType = msgDict[0]
            if(eventType == "startChallenge"):
                challengeHash = ""
                self.currentChallenge = challenge = {"prompt":msgDict[1]["prompt"],"text":msgDict[1]["text"]}
                if(challenge["text"] == None):
                    print("🖼️  > " + challenge["prompt"])
                    expectingImage = True
                else:
                    print("📄 > " + challenge["prompt"])
                    challengeHash = sha1(str(challenge))
                    answer = lookupAnswer(challengeHash)
                    print("❔ > No Answer" if (answer == None) else "✔️  > " + answer)
                    if (answer != None):legitType(answer,ws)
            elif(eventType == "endChallenge"):
                answer = msgDict[1]["source"]
                if(challengeHash != ""):
                    if(lookupAnswer(challengeHash) == None):
                        cacheAnswer(challengeHash, answer)
                        print("🏆 > " + answer)
            elif(eventType == "setMilestone"):
                if(msgDict[1]["name"] == "seating"):
                    print("🥇 > " + msgDict[1]["lastRound"]["winner"]["nickname"])
                    return

    def joinRoomCode(self,roomCode):
        print("⭐ > Connecting to chat...")
        self.connectToChat()
        print("🌟 > Connected to chat...")
        print("🔌 > Connecting to game...")
        self.connectToGame()
        print("💡 > Connected to game...")
        self.joinRound()
        print("⚡ > Joined round...")

    def joinRoom(self):
        self.joinRoomCode(self.roomCode)
