from control_commands import *
import time

sock = connect_bt()

prender_estereo(sock)
prender_cafetera(sock)
prender_tv(sock)
prender_luz_cuarto
prender_luz_sala(sock)
abrir_cochera(sock)

time.sleep(5)

cierra_sesion(sock)