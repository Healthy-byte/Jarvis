import PORTSCAN
import HOSTSCAN
import PASSWD
import SERVER
import IPLOOKUP
import sys
import html
import time
import subprocess
import art

spørgsmål = ["help", "navn", "dag", "system", "htmlU", "htmlE", "password", "portscan", "hostscan", "server", "iplookup"]

def main():
    global spørgsmål
    svartilbage = input("Spørg mig om noget: ")

    if svartilbage in spørgsmål:
        print("God kommando!")
    else:
        print("Din kommando giver ikke mening, skriv 'help' for at liste kommandoer")

    if svartilbage == "help":
        print("Du har følgende kommandoer")
        for i in spørgsmål:
            print (i, end= '\n')
    if svartilbage == "navn":
        art.tprint("HELLO", font="random")
        art.tprint("IM JARVIS", font="random")
    if svartilbage == "dag":
        ugedag = time.strftime("%A:%p")
        print("UGEDAG AM/PM: " + ugedag)
    if svartilbage == "system":
        print( "Platform: " + sys.platform)
    if svartilbage == "htmlU":
        hunesc = html.unescape(input("Skriv din HTML streng her: "))
        print ("Din HTML streng med UNESCAPE funktion: " + hunesc)
    if svartilbage == "htmlE":
        hesc = html.escape(input("Skriv din HTML streng her: "))
        print ("Din HTML streng med ESCAPE funktion: " + hesc)
# eksempel på html unescape funktion  &#73;&#110;&#118;&#105;&#110;&#99;&#105;&#98;&#108;&#101;&#72;&#97;&#99;&#107;&#51;&#114;
    
    if svartilbage == "portscan":
        ip_input = input ("Indtast din IP til Portscan: ")
        PORTSCAN.port_scanner(ip_input) 
    if svartilbage == "hostscan":
        host_input = input("Indtast din ip addresse - scanner kun sidste octet /24 netværk: ")
        HOSTSCAN.hostthreading(host_input)

    if svartilbage == "password":
        muligheder = ["check", "generate"]
        print("Du har følgende muligheder:")
        for i in muligheder:
            print(i, end= "\n")        
        valg = input("Vælg hilken funktion du vil bruge: ")
        if valg == "check":
            passwd_input = input("Skriv dit password her: ") + "\n"
            PASSWD.passchecker(passwd_input)
        if valg == "generate":
            passwd_input = input("Skriv dit password her: ")
            PASSWD.passgenerator(passwd_input)
    
    if svartilbage == "server":
        print("Du har nu følgende muligheder: ")
        muligheder2 = ["terminal", "hent", "send"]
        for i in muligheder2:
            print (i, end= "\n")
        valg = input ("Vælg hvilken service du vil bruge: ")
        if valg == "terminal":
            kommando = input("Skriv din terminal kommando her: ")
            cmd = subprocess.getstatusoutput(kommando)
            print(cmd)
        if valg == "send":
            end_ip = input("Skriv IP-adressen på den host du gerne vil sende til: ")
            fil_navn = input("Skriv navnet på filen du gerne vi sende: ")
            SERVER.send(end_ip,fil_navn)
        if valg == "hent":
            print ("GØR KLAR TIL AT HENTE, SERVICE ER OPPE I 5 MINUTTER")
            SERVER.hent()

    if svartilbage == "iplookup":
        IPLOOKUP.ip_lookup()
forever = True
while forever:
    main()