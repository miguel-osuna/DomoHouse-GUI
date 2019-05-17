from bluetooth import *

def connect_bt():
    bd_addr = "73:37:13:04:16:22"
    port = 1
    sock = BluetoothSocket(RFCOMM)
    sock.connect((bd_addr, port))
    return sock

def disconnect_bt(sock):
    sock.close()
    return None

def abrir_cochera(sock):
    print("Cochera abierta")
    sock.send("0")
    return None

def prender_cafetera(sock):
    print("Cafetera prendida")
    sock.send("1")
    return None

def prender_estereo(sock):
    print("Estereo prendido")
    sock.send("2")
    return None

def prender_tv(sock):
    print("Television prendida")
    sock.send("3")
    return None

def prender_luz_sala(sock):
    print("Luz de sala prendida")
    sock.send("4")
    return None

def prender_luz_cuarto(sock):
    print("Luz de cuarto prendida")
    sock.send("5")
    return None

def apaga_todo(sock):
    print("Todo apagado")
    sock.send("6")
    return None

def cierra_sesion(sock):
    print("Cierra sesion")
    sock.send("6")
    sock.send("7")
    return None

def inicia_sesion(sock):
    print("Inicia sesion")
    sock.send("8")

def id_confirmado(sock):
    bd_addr = "73:37:13:04:16:22"
    port = 1
    sock.bind(bd_addr, port)
    sock.listen(1)

    client_socket, address = sock.accept()
    data = sock.recv(1024)

    print(data)

    client_socket.close()
    sock.close()

    if data == '1':
        return True
    elif data == '0':
        return False

def userCarlos(sock):
    print("Carlos")
    abrir_cochera(sock)
    prender_cafetera(sock)
    prender_estereo(sock)
    return None

def userMiguel(sock):
    print("Miguel")
    prender_luz_cuarto(sock)
    prender_luz_sala(sock)
    prender_tv(sock)
    return None

def userMisael(sock):
    print("Misael")
    abrir_cochera(sock)
    prender_luz_cuarto(sock)
    prender_estereo(sock)
    return None

def userOptions(firstName, sock):
    if firstName is "Carlos":
        userCarlos(sock)
    elif firstName is "Miguel":
        userMiguel(sock)
    elif firstName is "Misael":
        userMisael(sock)
    else:
        print("Usuario Invalido")
    return None