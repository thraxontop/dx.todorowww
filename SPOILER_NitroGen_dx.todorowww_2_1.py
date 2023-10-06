import sys, time, threading
def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)


try:
    import colorama, requests
except:
    sys.stdout.write("> ")
    print015("Missing Required Modules, Press Enter To Download (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install colorama requests")
    except:
        pass
    sys.stdout.write("> ")
    print015("Problem Maybe Fixed Now, Restart The Program")
    input("")
    exit()



colorama.init(autoreset=True)






import os, threading
def set_title():
  title = "Nitro Gen/Checker by dx.todorowww"
  try:
    import requests
    text = str("")
    os.system(f"title {title}{text}")
  except:
    os.system(f"title {title}")
threading.Thread(target=set_title).start()




import random
import time

def valid():
    sys.stdout.write(colorama.Fore.RED + "RED ")
    print015("Enter A Valid Choice")
    return
while True:
    print(colorama.Fore.RED + """
     /$$   /$$ /$$   /$$                                  /$$$$$$
    | $$$ | $$|__/  | $$                                 /$$__  $$
    | $$$$| $$ /$$ /$$$$$$    /$$$$$$   /$$$$$$         | $$  \__/  /$$$$$$  /$$$$$$$
    | $$ $$ $$| $$|_  $$_/   /$$__  $$ /$$__  $$ /$$$$$$| $$ /$$$$ /$$__  $$| $$__  $$
    | $$  $$$$| $$  | $$    | $$  \__/| $$  \ $$|______/| $$|_  $$| $$$$$$$$| $$  \ $$
    | $$\  $$$| $$  | $$ /$$| $$      | $$  | $$        | $$  \ $$| $$_____/| $$  | $$
    | $$ \  $$| $$  |  $$$$/| $$      |  $$$$$$/        |  $$$$$$/|  $$$$$$$| $$  | $$
    |__/  \__/|__/   \___/  |__/       \______/          \______/  \_______/|__/  |__/
    


made by dx.todorowww
""")
    sys.stdout.write(colorama.Fore.WHITE + "> ")
    print(colorama.Fore.RED + "Want To Auto Check? (y/n): ")
    autocheck = input("")
    if autocheck == "y" or autocheck == "n":
        break
    else:
        valid()
while True:
    try:
        sys.stdout.write(colorama.Fore.WHITE + "> ")
        print(colorama.Fore.RED + "Enter delay: ")
        delay = input()
        delay = float(delay)
        break
    except Exception:
        valid()
while True:
    sys.stdout.write(colorama.Fore.WHITE + "> ")
    print(colorama.Fore.RED + "Auto Save (y/n): ")
    save = input("")
    if save == "n" or save == "y":
        break
    else:
        valid()
while True:
    try:
        sys.stdout.write(colorama.Fore.WHITE + "> ")
        print(colorama.Fore.RED + "Enter Amount To Generate/Check: ")
        limit = input("")
        limit = int(limit)
        break
    except Exception:
        valid()
if autocheck == "y":
    while True:
        sys.stdout.write(colorama.Fore.WHITE + "> ")
        print(colorama.Fore.RED + "Want Send Valid Codes To An Webhook (y/n): ")
        autowehook = input("")
        if autowehook == "y" or autowehook == "n":
            break
        else:
            valid()
    if autowehook == "y":
        while True:
            try:
                sys.stdout.write(colorama.Fore.WHITE + "> ")
                print01(colorama.Fore.RED + "Enter Webhook: ")
                webhook = input("")
                re = requests.get(webhook)
                re = str(re)
                if "200" in re:
                    break
                else:
                    sys.stdout.write(colorama.Fore.WHITE + "> ")
                    print015(colorama.Fore.GREEN + "Webhook Is Invalid")
            except Exception:
                sys.stdout.write(colorama.Fore.WHITE + "> ")
                print015("Webhook Invalid")
if autocheck == "n":
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    done = 0
    while True: 
        nn = random.choices(choices, k=16)
        code = "".join(nn)
        done = int(done) + 1
        print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} https://discord.gift/{colorama.Fore.CYAN}" + code)
        if save == "y":
            file = open("unchecked_nitro_codes.txt", "a")
            file.writelines("https://discord.gift/"+code+"\n")
            file.close()
        if int(done) == int(limit):
            sys.stdout.write(colorama.Fore.CYAN + "> ")
            print(colorama.Fore.RED + """
8888b.   dP"Yb  88b 88 888888 
 8I  Yb dP   Yb 88Yb88 88__   
 8I  dY Yb   dP 88 Y88 88""   
8888Y"   YbodP  88  Y8 888888 
""")
            print(colorama.Fore.RED + "Press Enter To Close The Program")
            input("")
            exit()
        time.sleep(float(delay))
if autocheck == "y":
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    done = 0
    while True: 
        nn = random.choices(choices, k=16)
        code = "".join(nn)
        r1 = requests.get("https://discordapp.com/api/v6/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
        r1 = str(r1)
        done = int(done) + 1
        if "200" in r1:
            print(f"{colorama.Fore.CYAN}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.CYAN}]{colorama.Fore.RESET} Generated Valid Code: https://discord.gift/{colorama.Fore.GREEN}" + code)
            if save == "y":
                file = open("valid_nitro_codes.txt", "a")
                file.writelines("https://discord.gift/"+code+"\n")
                file.close()
            while True:
                r2 = requests.post(webhook, json={"username": "Nitro Sniper", "content": "**Sniped A New Code:** "+code})
                r2 = str(r2)
                if "204" in r2:
                    sys.stdout.write(colorama.Fore.CYAN + "> ")
                    print015("Sent Code To Webhook")
                    break
                else:
                    sys.stdout.write(colorama.Fore.RED + "> ")
                    print("Ratelimited, Retrying...")

        if "200" not in r1:
            print(f"{colorama.Fore.RED}[{colorama.Fore.RESET}{str(done)}{colorama.Fore.RED}]{colorama.Fore.RESET} Generated Invalid Code: https://discord.gift/{colorama.Fore.RED}" + code)
            if save == "y":
                file = open("invalid_nitro_codes.txt", "a")
                file.writelines("https://discord.gift/"+code+"\n")
                file.close()
        if int(done) == int(limit):
            sys.stdout.write(colorama.Fore.RED + """
8888b.   dP"Yb  88b 88 888888 
 8I  Yb dP   Yb 88Yb88 88__   
 8I  dY Yb   dP 88 Y88 88""   
8888Y"   YbodP  88  Y8 888888 
""")
            print("\n\n")
            print(colorama.Fore.RED + "Press Enter To Close Program")
            input("")
            exit()
        time.sleep(float(delay))
