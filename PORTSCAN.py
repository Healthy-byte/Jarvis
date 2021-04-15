import socket
import threading
def tcp_forbinder(ip, port_number):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.settimeout(1)
    #succes = []
    try:
        a = TCPsock.connect_ex((ip, port_number))
        if a == 0:
            #succes.append(a)
            print("Port " + str(port_number) + ": OPEN")
    except:
        pass
def port_scanner(host_ip):
    
    
    threads = [] # tom liste

    for ports in range(10000):
        t = threading.Thread(target=tcp_forbinder, args=(host_ip, ports))
        threads.append(t) 
        #Her tilføjer alle de tråde der skal startes til ip'en
        #Dette bliver tilføjet til vores threads liste som vi kører alle sammen på samme tid senere hen
    
    for i in range(10000):
        threads[i].start()
        #Her starter vi alle de threads vi har gjort klart før
        #Disse threads bliver kaldt ved hjælp af indekseringen [i]

    for i in range(10000):
        threads[i].join()
        #Dette er noget der skal være med da det låser vores threads
        #indtil de er færdigkørte, her kan join statement godt være
        #lidt forvirrende men hvis du læser funktionen igennem giver
        #det mening
    #for i in range(10000):
        #if udskrift[i] == 0:
            #print("Port: " + str(i) + " er åben")
        #Du skal kigge på de argumenter der bliver givet oppe i første
        #For lykke. Hvis vores try lykkeds er det == "Der er forbindelse"
        #Og det givende nummer bliver printet. Smart smart