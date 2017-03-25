def handle(msg, bot, reimport):
    import json
    import telepot
    import time
    import configfile
    import random
    import os
    try:
        botid = configfile.botid
    except:
        botid = "@EagleGangBot"
    botid = botid.lower()
    banamount = 10
    #print("reloaded")
    #print(msg)
    #json.dump(msg, open("dump" + str(time.clock()) + ".txt", "w"))
    def limit(derwert, daslimit):
        if(derwert >= daslimit):
            return daslimit
        else:
            return derwert
    
    try:
        users = json.load(open("users.json"))
    except:
        users = {"nobody" : "0"}
        print("fehler 1")
    try:
        print(msg["from"]["username"] + " : " + str(msg["from"]["id"]))
        if(not msg["from"]["username"] in users):
            users[msg["from"]["username"]] = msg["from"]["id"]
    except:
        print("fehler 2 (Er hat keinen Nutzernamen)")
    try:
        json.dump(users, open("users.json", "w"))
        id = msg["chat"]["id"]
    except:
        print("fehler 3")
    #id = msg["from"]["id"]
    try:
        realtext = msg["text"]
        command = msg["text"].lower().split(" ")[0]
    except:
        bot.sendMessage(id, "Sorry, i am not yet ready to interact with this")
    if("entities" in msg and "type" in msg["entities"][0] and msg["entities"][0]["type"] == "bot_command" and command[0] == "/"):
        if(True):
            if(command == "/help" or command == "/help" + botid):
                try:
                    bot.sendMessage(id, open(configfile.helpfile).read())
                except:
                    pass
            elif(command == "/reload" or command == "/reload" + botid):
                return reimport(id)
            elif(command == "/zitat" or command == "/zitat" + botid):
                try:
                    bot.sendMessage(id, random.choice(open(configfile.zitatfile).readlines()))
                except:
                    pass
            elif(command == "/tutorial" or command == "/tutorial" + botid or command == "/needtutorial" or command == "/needtutorial" + botid):
                try:
                    bot.sendMessage(id, open(configfile.tutfile).read())
                except:
                    pass
            elif(command == "/brucelee" or command == "/brucelee" + botid):
                try:
                    bot.sendMessage(id, random.choice(open(configfile.brucefile).readlines()))
                except:
                    pass
            elif(command == "/penis" or command == "/penis" + botid):
                try:
                    bot.sendMessage(id, "<" + "=" * limit(int(realtext.split(" ")[1]), 500) + "3")
                except:
                    bot.sendMessage(id, "<====3")
            elif(command == "/love" or command == "/love" + botid):
                bot.sendMessage(id, "<3")
            elif(command == "/sendnudes" or command == "/sendnudes" + botid):
                try:
                    if(configfile.usenudefile):
                        bot.sendMessage(id, open(configfile.nudefile).read())
                    else:
                        bot.sendPhoto(id, open(config.nudefolder + random.choice(os.listdir(config.nudefolder))), caption="Dat Nude!")
                except:
                    pass
            elif(command == "/glasfaserbiszumhaus" or command == "/glasfaserbiszumhaus" + botid):
                bot.sendMessage(id, "glasfaserbiszumcomputer")
            elif(command == "/omnivoren" or command == "/omnivoren" + botid):
                bot.sendMessage(id, "lachaft")
            elif(command == "/vegans" or command == "/vegans" + botid or command == "/veganer" or command == "/veganer" + botid):
                bot.sendMessage(id, "VEGANER SIND FUCKING GAY! NIGERIANISCHER PRINZ.")
            elif(command == "/web" or command == "/web" + botid):
                try:
                    bot.sendMessage(id, configfile.weburl)
                except:
                    pass
            else:
                bot.sendMessage(id, "Sorry, no recognizeable command. Use /help instead")
                #bot.sendMessage(id, raw_input(msg["text"] + ": "))
    else:
        try:
            if("xD" in msg["text"] or "XD" in msg["text"] or "xd" in msg["text"] or "Xd" in msg["text"]):
                bot.sendMessage(id, u'\U0001f606')
            elif("nein" in msg["text"] or "Nein" in msg["text"]):
                bot.sendMessage(id, "Doch")
        except:
            pass
