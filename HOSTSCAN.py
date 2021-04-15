import subprocess
import os
import threading

def hostscanner(IP):
    cmd_kommando = "ping -n 1 -w 20 " + IP # -n er antal gange -w er ms
    DEVNULL = open(os.devnull, "w") #Skraldespand vaiabel
    svar = subprocess.call(cmd_kommando, stdout=DEVNULL)
    if svar == 0:
        print ("Host: " + IP +" er oppe")        

def hostthreading(ip_input):
    threads = []
    ip_sidste_octet = ip_input.split(".")
    for ip_sidste_octet[3] in range(0,255): #Dette tager data fra arrayets 3 indeksering dvs. 4 plads
        ip_til_scan = ".".join(map(str, ip_sidste_octet))
        t = threading.Thread(target=hostscanner, args=(ip_til_scan,))
        threads.append(t)
    for i in range (0,255):
        threads[i].start()
    for i in range (0,255):
        threads[i].join
            
