import socket
import subprocess
import tqdm
import os

def send (host_ip_input, filnavn_input):
    seperator = "<SEPERATOR>"
    buffer_size = 4096 #Hvor meget du vil sende af data af gangen (bytes)
    port = 9999
    folder_name = os.path.dirname(os.path.abspath(__file__)) #Giver os den fulde sti på SERVER.py filen
    endelig_fil = os.path.join(folder_name, filnavn_input)
    file_size = os.path.getsize(endelig_fil) #Hvade filnavn_input stående her i lang tid og det var grunden til det ikke virkede
    print ("Din fil er " + str(file_size) + " bytes")
    s = socket.socket()
    print(f"Connecter til {host_ip_input}:{port}")
    s.connect((host_ip_input, port))
    print("CONNECTED")
    #print (f"{endelig_fil}{seperator}{file_size}")
    s.send(f"{endelig_fil}{seperator}{file_size}".encode())
    print(f"{endelig_fil}{seperator}{file_size}")
    load_bar = tqdm.tqdm(range(file_size), f"SENDER: {endelig_fil}", unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(endelig_fil, "rb") as fil:
        while True:
            bytes_der_læses = fil.read(buffer_size) #Læser bytes med 4096 bytes af gangen
            if not bytes_der_læses: #Hvis hele filen er læst
                load_bar.update(len(bytes_der_læses))
                break
            s.sendall(bytes_der_læses)
            load_bar.update(len(bytes_der_læses))
    load_bar.close()
    s.close()

def hent():
    print("Sætter server op til at lytte på alle forbindelser!")
    #Der skal eventuelt laves input her så man kun vil lytte på en specifik IP
    seperator = "<SEPERATOR>"
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 9999
    buffer_size = 4096
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    klient_socket, accepterede_forbindelse = s.accept()
    # Accept a connection. The socket must be bound to an address and listening for connections. 
    # The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, 
    # and address is the address bound to the socket on the other end of the connection.
    print (f"{accepterede_forbindelse} er forbundet")
    modtaget = klient_socket.recv(buffer_size).decode()
    endelig_fil, file_size = modtaget.split(seperator)
    fil_navn = os.path.basename(endelig_fil)
    #Vi fjerner sti navnet så der ikke er C:\xxx\xxx\xxxxx\ osv. 
    file_size = int(file_size)

    #Vi er nu klar til at skrive den data vi modtage ud i en fil
    load_bar = tqdm.tqdm(range(file_size), f"MODTAGER: {fil_navn}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(fil_navn, "wb") as fil:
        while True:
            bytes_der_læses = klient_socket.recv(buffer_size)
            if not bytes_der_læses: 
                load_bar.update(len(bytes_der_læses))
                break
            fil.write(bytes_der_læses)
            load_bar.update(len(bytes_der_læses))

    load_bar.close()
    klient_socket.close()
    s.close()