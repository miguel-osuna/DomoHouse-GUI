import bluetooth


def connect_bt():
    bd_addr = "73:37:13:04:16:22"
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))
    return None


def disconnect_bt():
    sock.close
    return None


def abrir_cochera():
    print("Cochera abierta")
    sock.send(0)
    return None


def cerrar_cochera():
    print("Cochera cerrada")
    sock.send(1)
    return None


def prender_cafetera():
    print("Cafetera prendida")
    sock.send(2)
    return None


def apagar_cafetera():
    print("Cafetera apagada")
    sock.send(3)
    return None


def prender_estereo():
    print("Estereo prendido")
    sock.send(4)
    return None


def apagar_estereo():
    print("Estero apagado")
    sock.send(5)
    return None


def prender_tv():
    print("Television prendida")
    sock.send(6)
    return None


def apagar_tv():
    print("Television apagada")
    sock.send(7)
    return None


def prender_luz_sala():
    print("Luz de sala prendida")
    sock.send(8)
    return None


def apagara_luz_sala():
    print("Luz de sala apagada")
    sock.send(9)
    return None


def prender_luz_cuarto():
    print("Luz de cuarto prendida")
    sock.send(10)
    return None


def apagar_luz_cuarto():
    print("Luz de cuarto apagada")
    sock.send(11)
    return None


def apaga_todo():
    apagar_luz_cuarto()
    apagar_luz_sala()
    apagar_tv()
    apagar_estereo()
    apagar_cafetera()
    apagar_cochera()
    return None


def userCarlos():
    print("Carlos")
    # abrir_cochera()
    # prender_cafetera()
    # prender_estereo()
    return None


def userMiguel():
    print("Miguel")
    # prender_luz_cuarto()
    # prender_luz_sala()
    # prender_tv()
    return None


def userMisael():
    print("Misael")
    # abrir_cochera()
    # prender_luz_cuarto()
    # prender_estereo()
    return None


def userOptions(firstName):
    if firstName is "Carlos":
        userCarlos()
    elif firstName is "Miguel":
        userMiguel()
    elif firstName is "Misael":
        userMisael()
    else:
        print("Usuario Invalido")
