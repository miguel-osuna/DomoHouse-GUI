from control_commands import *
from photo_commands import *
import time

sock = connect_bt()

'''prender_estereo(sock)
prender_cafetera(sock)
prender_tv(sock)
prender_luz_cuarto
prender_luz_sala(sock)
abrir_cochera(sock)
'''

inicia_sesion(sock)
apaga_todo(sock)

time.sleep(5)

# takeSnapshotAndSave(1)